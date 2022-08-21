from datetime import datetime, timedelta
import jwt

from django.conf import settings


def get_token_pair(user):
    datetime_issued_at = datetime.now()
    datetime_refresh_expires_at = datetime_issued_at + timedelta(days=1)
    datetime_access_expires_at = datetime_issued_at + timedelta(minutes=10)

    jwt_access_token_payload = {
        "type": "access",
        "exp": datetime_access_expires_at.timestamp(),
        "iat": datetime_issued_at.timestamp(),
        "user_id": str(user.id),
    }
    jwt_refresh_token_payload = {
        'type': 'refresh',
        'exp': datetime_refresh_expires_at.timestamp(),
        'iat': datetime_issued_at.timestamp(),
        "user_id": str(user.id),
    }
    access_token = jwt.encode(
        jwt_access_token_payload, key=settings.SECRET_KEY)
    refresh_token = jwt.encode(
        jwt_refresh_token_payload, key=settings.SECRET_KEY)
    return access_token, refresh_token
