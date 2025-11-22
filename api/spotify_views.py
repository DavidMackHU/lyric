"""
Spotify and Lyrics API views
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .spotify_service import SpotifyService
from .lyrics_service import LyricsService


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_spotify(request):
    """Search for songs on Spotify"""
    query = request.query_params.get('q', '')
    limit = int(request.query_params.get('limit', 20))
    
    if not query:
        return Response({'error': 'Query parameter "q" is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    service = SpotifyService()
    result = service.search_songs(query, limit)
    
    return Response(result)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_track_details(request, track_id):
    """Get detailed information about a Spotify track"""
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
    
    service = LyricsService()
    lyrics = service.get_lyrics(artist, song)
    
    if not lyrics:
        return Response(
            {'error': 'Lyrics not found for this song'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    return Response({'lyrics': lyrics})


