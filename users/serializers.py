from django.contrib.auth import get_user_model
from rest_framework.serializers import HyperlinkedModelSerializer

User = get_user_model()


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'email']
