from rest_framework import serializers
from .models import User, Challenge, ChallengeAttempt


class UserSerializer(serializers.ModelSerializer):
    created_challenges = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'firebase_uid', 'total_score', 
                  'accuracy', 'songs_played', 'created_challenges', 'created_at']
        read_only_fields = ['id', 'created_at']

    def get_created_challenges(self, obj):
        return obj.created_challenges.count()


class ChallengeSerializer(serializers.ModelSerializer):
    creator_name = serializers.CharField(source='creator.username', read_only=True)

    class Meta:
        model = Challenge
        fields = ['id', 'creator', 'creator_name', 'song_title', 'artist', 
                  'spotify_id', 'genre', 'lyric_snippet', 'blanked_text', 
                  'correct_answer', 'hint', 'created_at', 'is_public']
        read_only_fields = ['id', 'creator', 'created_at']


class ChallengeListSerializer(serializers.ModelSerializer):
    """Serializer for listing challenges without revealing answers"""
    creator_name = serializers.CharField(source='creator.username', read_only=True)

    class Meta:
        model = Challenge
        fields = ['id', 'creator_name', 'song_title', 'artist', 'spotify_id', 
                  'genre', 'blanked_text', 'created_at']


class ChallengeAttemptSerializer(serializers.ModelSerializer):
    challenge_title = serializers.CharField(source='challenge.song_title', read_only=True)

    class Meta:
        model = ChallengeAttempt
        fields = ['id', 'user', 'challenge', 'challenge_title', 'user_answer', 
                  'is_correct', 'score_earned', 'attempts_count', 'hint_used', 
                  'completed_at']
        read_only_fields = ['id', 'user', 'completed_at']


