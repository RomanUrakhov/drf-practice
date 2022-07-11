from unicodedata import name
from django.db import models
from django.utils.timezone import now
from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=25)
    repo_link = models.URLField()
    users = models.ManyToManyField(User)

    def __str__(self) -> str:
        return f"{self.pk}. {self.name}"


class Todo(models.Model):
    project = models.ForeignKey(Project, models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=64)
    todo_text = models.TextField(max_length=500)
    is_closed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=now, editable=False)
    updated_date = models.DateTimeField(default=now, editable=False)
