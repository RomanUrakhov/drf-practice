from django.db import models
from django.utils.timezone import now
from django.conf import settings


class Project(models.Model):
    name = models.CharField(max_length=25)
    repo_link = models.URLField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self) -> str:
        return f"{self.pk}. {self.name}"


class Todo(models.Model):
    project = models.ForeignKey(Project, models.PROTECT)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=64)
    todo_text = models.TextField(max_length=500)
    is_closed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=now, editable=False)
    updated_date = models.DateTimeField(default=now, editable=False)
