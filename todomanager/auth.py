from django.conf import settings
import jwt
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

User = get_user_model()


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None
        try:
            access_token = auth_header.split(' ')[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])
        except IndexError:
            raise exceptions.AuthenticationFailed(
                detail='Token prefix not provided')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                detail='access_token has expired')

        try:
            found_user = User.objects.get(
                id=payload['user_id'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(detail='User not found')

        return (found_user, None)
