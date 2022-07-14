from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    # TODO: figure out what about password field
    class Meta:
        model = User
        fields = ['id', 'url', 'login']
