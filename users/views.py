from rest_framework.viewsets import GenericViewSet
from .models import User
from .serializers import UserModelSerializer
from rest_framework import mixins


class UserModelCustomViewSet(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.ListModelMixin,
                             GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
