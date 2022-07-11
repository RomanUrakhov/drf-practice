from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Project, Todo
from .serializers import ProjectSerializer, TodoSerializer
from .pagination import ProjectPageNumberPagination, TodoPageNumberPagination
from .filters import ProjectModelFilter, TodoModelFilter


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectPageNumberPagination
    filterset_class = ProjectModelFilter


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filterset_class = TodoModelFilter
    pagination_class = TodoPageNumberPagination

    def destroy(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        instance.is_closed = True
        serializer = TodoSerializer(instance, context={'request': request})
        instance.save()
        return Response(serializer.data)
