from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q
from .models import User, Challenge, ChallengeAttempt
from .serializers import (
    UserSerializer, ChallengeSerializer, ChallengeListSerializer, 
    ChallengeAttemptSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def profile(self, request):
        """Get current user's profile with calculated accuracy"""
        user = request.user
        
        # Calculate accuracy from attempts
        total_attempts = ChallengeAttempt.objects.filter(user=user).count()
        correct_attempts = ChallengeAttempt.objects.filter(user=user, is_correct=True).count()
        
        if total_attempts > 0:
            accuracy = (correct_attempts / total_attempts) * 100
            # Update user's accuracy if it's different
            if abs(user.accuracy - accuracy) > 0.01:
                user.accuracy = accuracy
                user.save()
        else:
            accuracy = user.accuracy
        
        serializer = self.get_serializer(user)
        data = serializer.data
        data['accuracy'] = accuracy  # Ensure calculated accuracy is returned
        return Response(data)

    @action(detail=False, methods=['post'])
    def create_profile(self, request):
        """Create or update user profile from Firebase"""
        firebase_uid = request.data.get('firebase_uid')
        email = request.data.get('email')
        username = request.data.get('username', email)

        if not firebase_uid:
            return Response(
                {'error': 'firebase_uid is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Get or create user by Firebase UID
        user, created = User.objects.get_or_create(
            firebase_uid=firebase_uid,
            defaults={
                'username': username or firebase_uid,
                'email': email or '',
            }
        )

        # If user already exists, update if authenticated user matches
        if not created:
            # Verify Firebase UID matches authenticated user (if user is authenticated)
            if hasattr(request, 'user') and request.user.is_authenticated:
                if request.user.firebase_uid != firebase_uid and request.user.id != user.id:
                    return Response(
                        {'error': 'Firebase UID does not match authenticated user'}, 
                        status=status.HTTP_403_FORBIDDEN
                    )
            
            # Update existing user if new data provided
            updated = False
            if email and email != user.email:
                user.email = email
                updated = True
            if username and username != user.username:
                user.username = username
                updated = True
            if updated:
                user.save()

        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Get user statistics including calculated accuracy"""
        user = request.user
        
        # Calculate accuracy from attempts
        total_attempts = ChallengeAttempt.objects.filter(user=user).count()
        correct_attempts = ChallengeAttempt.objects.filter(user=user, is_correct=True).count()
        
        if total_attempts > 0:
            accuracy = (correct_attempts / total_attempts) * 100
            user.accuracy = accuracy
            user.save()
        else:
            accuracy = 0.0
        
        return Response({
            'total_score': user.total_score,
            'songs_played': user.songs_played,
            'accuracy': accuracy,
            'created_challenges': user.created_challenges.count(),
            'total_attempts': total_attempts,
            'correct_attempts': correct_attempts,
        })


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.filter(is_public=True)
    permission_classes = [AllowAny]  # Allow viewing, require auth for creating

    def get_queryset(self):
        """Return challenges based on action and user"""
        if self.action == 'list':
            return Challenge.objects.filter(is_public=True)
        elif self.action in ['update', 'partial_update', 'destroy']:
            # Users can only edit/delete their own challenges
            if self.request.user.is_authenticated:
                return Challenge.objects.filter(creator=self.request.user)
            return Challenge.objects.none()
        return Challenge.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ChallengeListSerializer
        return ChallengeSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def submit_answer(self, request, pk=None):
        """Submit an answer to a challenge"""
        challenge = self.get_object()
        user_answer = request.data.get('answer', '').strip()
        hint_used = request.data.get('hint_used', False)

        if not user_answer:
            return Response(
                {'error': 'Answer is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Get or create attempt
        attempt, created = ChallengeAttempt.objects.get_or_create(
            user=request.user,
            challenge=challenge,
            defaults={
                'user_answer': user_answer,
                'attempts_count': 1,
                'hint_used': hint_used,
            }
        )

        if not created:
            attempt.attempts_count += 1
            attempt.user_answer = user_answer
            if hint_used:
                attempt.hint_used = True
            attempt.save()

        # Check if answer is correct (simple comparison, can be enhanced)
        is_correct = self._check_answer(user_answer, challenge.correct_answer)
        attempt.is_correct = is_correct

        # Calculate score
        if is_correct:
            base_score = 100
            if hint_used:
                base_score = int(base_score * 0.5)  # Reduce score if hint used
            attempt.score_earned = max(0, base_score - (attempt.attempts_count - 1) * 10)
            
            # Update user stats
            request.user.total_score += attempt.score_earned
            request.user.songs_played += 1
            
            # Recalculate accuracy
            total_attempts = ChallengeAttempt.objects.filter(user=request.user).count()
            correct_attempts = ChallengeAttempt.objects.filter(user=request.user, is_correct=True).count()
            if total_attempts > 0:
                request.user.accuracy = (correct_attempts / total_attempts) * 100
            
            request.user.save()
        else:
            attempt.score_earned = 0

        attempt.save()

        serializer = ChallengeAttemptSerializer(attempt)
        return Response(serializer.data)

    def _check_answer(self, user_answer, correct_answer):
        """Check if user answer matches correct answer (with some flexibility)"""
        # Normalize both answers
        user_normalized = user_answer.lower().strip()
        correct_normalized = correct_answer.lower().strip()
        
        # Exact match
        if user_normalized == correct_normalized:
            return True
        
        # Check if user answer is contained in correct answer or vice versa
        # (for partial matches)
        if user_normalized in correct_normalized or correct_normalized in user_normalized:
            return True
        
        return False

    @action(detail=True, methods=['get'], permission_classes=[AllowAny])
    def hint(self, request, pk=None):
        """Get hint for a challenge"""
        challenge = self.get_object()
        return Response({'hint': challenge.hint})


class LeaderboardViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        """Get global leaderboard with optional filtering"""
        genre = request.query_params.get('genre', None)
        date_filter = request.query_params.get('date', None)
        
        queryset = User.objects.filter(total_score__gt=0)
        
        # Filter by genre (if challenges have genre info)
        if genre:
            # This would require joining with challenges - simplified for now
            pass
        
        # Order by score
        queryset = queryset.order_by('-total_score')[:100]
        
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


# Spotify and Lyrics API endpoints
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_spotify(request):
    """Search for songs on Spotify"""
    query = request.query_params.get('q', '')
    limit = int(request.query_params.get('limit', 20))
    
    if not query:
        return Response({'error': 'Query parameter "q" is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    from .spotify_service import SpotifyService
    service = SpotifyService()
    result = service.search_songs(query, limit)
    
    return Response(result)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_track_details(request, track_id):
    """Get detailed information about a Spotify track"""
    from .spotify_service import SpotifyService
    service = SpotifyService()
    result = service.get_track_details(track_id)
    
    if 'error' in result:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(result)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_lyrics(request):
    """Get lyrics for a song"""
    artist = request.query_params.get('artist', '')
    song = request.query_params.get('song', '')
    
    if not artist or not song:
        return Response(
            {'error': 'Both "artist" and "song" parameters are required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    from .lyrics_service import LyricsService
    service = LyricsService()
    lyrics = service.get_lyrics(artist, song)
    
    if not lyrics:
        return Response(
            {'error': 'Lyrics not found for this song'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    return Response({'lyrics': lyrics})

