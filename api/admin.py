from django.contrib import admin
from .models import User, Challenge, ChallengeAttempt


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'firebase_uid', 'total_score', 'songs_played']
    search_fields = ['username', 'email', 'firebase_uid']


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['song_title', 'artist', 'creator', 'created_at', 'is_public']
    list_filter = ['is_public', 'created_at']
    search_fields = ['song_title', 'artist', 'creator__username']


@admin.register(ChallengeAttempt)
class ChallengeAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'challenge', 'is_correct', 'score_earned', 'completed_at']
    list_filter = ['is_correct', 'completed_at']
    search_fields = ['user__username', 'challenge__song_title']


