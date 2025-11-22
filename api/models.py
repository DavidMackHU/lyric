from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Extended user model with Firebase UID and game stats"""
    firebase_uid = models.CharField(max_length=128, unique=True, null=True, blank=True)
    total_score = models.IntegerField(default=0)
    accuracy = models.FloatField(default=0.0)
    songs_played = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'


class Challenge(models.Model):
    """Lyric challenge model"""
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_challenges')
    song_title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    spotify_id = models.CharField(max_length=128, unique=True)
    genre = models.CharField(max_length=100, blank=True)
    lyric_snippet = models.TextField()
    blanked_text = models.TextField()  # The lyric with blanks
    correct_answer = models.TextField()  # The correct missing lyric
    hint = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    class Meta:
        db_table = 'challenges'
        ordering = ['-created_at']


class ChallengeAttempt(models.Model):
    """User attempt at a challenge"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attempts')
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='attempts')
    user_answer = models.TextField()
    is_correct = models.BooleanField(default=False)
    score_earned = models.IntegerField(default=0)
    attempts_count = models.IntegerField(default=1)
    hint_used = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'challenge_attempts'
        unique_together = ['user', 'challenge']
        ordering = ['-completed_at']


