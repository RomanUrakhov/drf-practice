import imp
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Project, Todo
from users.serializers import UserModelSerializer


class ProjectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "url", "name", "repo_link"]


class TodoSerializer(HyperlinkedModelSerializer):
    project = ProjectSerializer()
    author = UserModelSerializer()

    class Meta:
        model = Todo
        fields = ['id', 'url', 'todo_name', 'project', 'todo_text', 'is_closed', 'author', 'created_date', 'updated_date']
