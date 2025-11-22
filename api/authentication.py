from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
import firebase_admin
from firebase_admin import credentials, auth as firebase_auth
from django.conf import settings
import os


# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    cred_path = settings.FIREBASE_CREDENTIALS_PATH
    if cred_path and os.path.exists(cred_path):
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    else:
        # For development, you can use default credentials
        # In production, always use service account credentials
        try:
            firebase_admin.initialize_app()
        except ValueError:
            # Already initialized
            pass


class FirebaseAuthentication(authentication.BaseAuthentication):
    """Custom authentication using Firebase tokens"""

    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        
        if not auth_header.startswith('Bearer '):
            return None

        token = auth_header.split('Bearer ')[1]

        try:
            decoded_token = firebase_auth.verify_id_token(token)
            firebase_uid = decoded_token['uid']
            
            # Get or create user
            from .models import User
            user, _ = User.objects.get_or_create(
                firebase_uid=firebase_uid,
                defaults={
                    'username': decoded_token.get('email', firebase_uid),
                    'email': decoded_token.get('email', ''),
                }
            )
            
            return (user, None)
        except Exception as e:
            raise AuthenticationFailed(f'Invalid Firebase token: {str(e)}')


