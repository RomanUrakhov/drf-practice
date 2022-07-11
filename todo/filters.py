from dataclasses import fields
from pyexpat import model
import django_filters

from .models import Project, Todo


class ProjectModelFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = {
            'name': ['icontains']
        }


class TodoModelFilter(django_filters.FilterSet):
    project = django_filters.ModelChoiceFilter(queryset=Project.objects.all())

    class Meta:
        model = Todo
        fields = ['project']
