from django.conf import settings
from django.contrib.auth import get_user_model
import jwt
from rest_framework.viewsets import GenericViewSet

from users.utils import get_token_pair
from .serializers import UserModelSerializer
from rest_framework import mixins, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny

User = get_user_model()


class UserModelCustomViewSet(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.ListModelMixin,
                             GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class JWTGeneratePairView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            raise exceptions.AuthenticationFailed('Incorrect credentials')
        try:
            found_user: User = User.objects.get(email=email)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not found')

        if not found_user.is_active:
            raise exceptions.AuthenticationFailed('User is not active')

        if not found_user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed('Incorrect credentials')

        access_token, refresh_token = get_token_pair(found_user)
        return Response({'access_token': access_token, 'refresh_token': refresh_token})


class JWTRefreshView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request):
        refresh_token = request.data.get('refresh_token')
        if refresh_token is None:
            raise exceptions.AuthenticationFailed(
                detail='Refresh token is not provided')
        try:
            payload = jwt.decode(
                refresh_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                'Refresh token has expired. Please re-login')
        try:
            user = User.objects.get(id=payload['user_id'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User is not active')

        access_token, _ = get_token_pair(user)
        return Response({'access_token': access_token})
