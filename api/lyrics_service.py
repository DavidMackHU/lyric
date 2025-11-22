"""
Lyrics service for retrieving song lyrics
Uses multiple free APIs as fallback
"""
import requests
import logging

logger = logging.getLogger(__name__)


class LyricsService:
    """Service for retrieving song lyrics from various sources"""
    
    def __init__(self):
        self.timeout = 5
    
    def get_lyrics(self, artist, song_title):
        """
        Get lyrics for a song using multiple sources as fallback
        Returns lyrics text or None if not found
        """
        # Try lyrics.ovh API first (free, no API key needed)
        lyrics = self._get_from_lyrics_ovh(artist, song_title)
        if lyrics:
            return lyrics
        
        # Try api.lyrics.ovh as alternative
        lyrics = self._get_from_api_lyrics_ovh(artist, song_title)
        if lyrics:
            return lyrics
        
        # Try lyricsgenius fallback (would need API key)
        # For now, return None if not found
        return None
    
    def _get_from_lyrics_ovh(self, artist, song_title):
        """Get lyrics from lyrics.ovh API"""
        try:
            # Clean artist and song title
            artist_clean = artist.split(',')[0].strip()  # Take first artist
            song_clean = song_title.strip()
            
            url = f'https://api.lyrics.ovh/v1/{artist_clean}/{song_clean}'
            response = requests.get(url, timeout=self.timeout)
            
            if response.status_code == 200:
                data = response.json()
                lyrics = data.get('lyrics', '')
                if lyrics and len(lyrics) > 10:  # Basic validation
                    return lyrics
        except Exception as e:
            logger.debug(f"lyrics.ovh failed: {str(e)}")
        
        return None
    
    def _get_from_api_lyrics_ovh(self, artist, song_title):
        """Alternative lyrics source"""
        try:
            artist_clean = artist.split(',')[0].strip()
            song_clean = song_title.strip()
            
            url = f'https://lyrics.ovh/v1/{artist_clean}/{song_clean}'
            response = requests.get(url, timeout=self.timeout)
            
            if response.status_code == 200:
                data = response.json()
                lyrics = data.get('lyrics', '')
                if lyrics and len(lyrics) > 10:
                    return lyrics
        except Exception as e:
            logger.debug(f"Alternative lyrics API failed: {str(e)}")
        
        return None
    
    def extract_lyric_snippet(self, full_lyrics, max_length=200):
        """Extract a snippet from full lyrics"""
        if not full_lyrics:
            return None
        
        # Remove common metadata lines
        lines = full_lyrics.split('\n')
        clean_lines = []
        
        for line in lines:
            line = line.strip()
            # Skip empty lines and common metadata
            if line and not any(skip in line.lower() for skip in ['[verse', '[chorus', '[bridge', '[intro', '[outro']):
                clean_lines.append(line)
        
        # Take first few lines that fit in max_length
        snippet = ''
        for line in clean_lines[:10]:  # Max 10 lines
            if len(snippet) + len(line) + 1 <= max_length:
                snippet += line + '\n'
            else:
                break
        
        return snippet.strip() if snippet else None


