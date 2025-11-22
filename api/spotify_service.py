"""
Spotify API service for searching songs
"""
import requests
import base64
from django.conf import settings
from decouple import config
import logging

logger = logging.getLogger(__name__)


class SpotifyService:
    """Service for interacting with Spotify Web API"""
    
    def __init__(self):
        self.client_id = config('SPOTIFY_CLIENT_ID', default='')
        self.client_secret = config('SPOTIFY_CLIENT_SECRET', default='')
        self.token_url = 'https://accounts.spotify.com/api/token'
        self.api_base_url = 'https://api.spotify.com/v1'
        self._access_token = None
    
    def _get_access_token(self):
        """Get Spotify access token using client credentials"""
        if self._access_token:
            return self._access_token
        
        if not self.client_id or not self.client_secret:
            logger.warning("Spotify credentials not configured")
            return None
        
        try:
            # Encode credentials
            credentials = f"{self.client_id}:{self.client_secret}"
            encoded_credentials = base64.b64encode(credentials.encode()).decode()
            
            # Request token
            headers = {
                'Authorization': f'Basic {encoded_credentials}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            data = {'grant_type': 'client_credentials'}
            
            response = requests.post(self.token_url, headers=headers, data=data, timeout=5)
            response.raise_for_status()
            
            token_data = response.json()
            self._access_token = token_data['access_token']
            return self._access_token
        except Exception as e:
            logger.error(f"Error getting Spotify token: {str(e)}")
            return None
    
    def search_songs(self, query, limit=20):
        """Search for songs on Spotify"""
        token = self._get_access_token()
        if not token:
            return {'error': 'Spotify API not configured'}
        
        try:
            headers = {'Authorization': f'Bearer {token}'}
            params = {
                'q': query,
                'type': 'track',
                'limit': limit
            }
            
            response = requests.get(
                f'{self.api_base_url}/search',
                headers=headers,
                params=params,
                timeout=5
            )
            response.raise_for_status()
            
            data = response.json()
            tracks = []
            
            for item in data.get('tracks', {}).get('items', []):
                track = {
                    'id': item['id'],
                    'name': item['name'],
                    'artist': ', '.join([artist['name'] for artist in item['artists']]),
                    'album': item['album']['name'],
                    'preview_url': item.get('preview_url'),
                    'external_url': item['external_urls']['spotify'],
                    'image_url': item['album']['images'][0]['url'] if item['album']['images'] else None,
                    'duration_ms': item['duration_ms'],
                }
                tracks.append(track)
            
            return {'tracks': tracks}
        except Exception as e:
            logger.error(f"Error searching Spotify: {str(e)}")
            return {'error': f'Failed to search Spotify: {str(e)}'}
    
    def get_track_details(self, track_id):
        """Get detailed information about a specific track"""
        token = self._get_access_token()
        if not token:
            return {'error': 'Spotify API not configured'}
        
        try:
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get(
                f'{self.api_base_url}/tracks/{track_id}',
                headers=headers,
                timeout=5
            )
            response.raise_for_status()
            
            item = response.json()
            track = {
                'id': item['id'],
                'name': item['name'],
                'artist': ', '.join([artist['name'] for artist in item['artists']]),
                'album': item['album']['name'],
                'preview_url': item.get('preview_url'),
                'external_url': item['external_urls']['spotify'],
                'image_url': item['album']['images'][0]['url'] if item['album']['images'] else None,
                'duration_ms': item['duration_ms'],
                'genres': item['album'].get('genres', []),
            }
            
            return track
        except Exception as e:
            logger.error(f"Error getting track details: {str(e)}")
            return {'error': f'Failed to get track details: {str(e)}'}


