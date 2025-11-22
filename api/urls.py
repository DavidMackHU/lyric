from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .views import (
    UserViewSet, ChallengeViewSet, LeaderboardViewSet,
    search_spotify, get_track_details, get_lyrics
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'challenges', ChallengeViewSet, basename='challenge')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """Health check endpoint to test API connection"""
    return Response({'status': 'ok', 'message': 'LyrIQ API is running'})

urlpatterns = [
    path('health/', health_check, name='health-check'),
    path('spotify/search/', search_spotify, name='spotify-search'),
    path('spotify/track/<str:track_id>/', get_track_details, name='spotify-track'),
    path('lyrics/', get_lyrics, name='get-lyrics'),
    path('', include(router.urls)),
]

