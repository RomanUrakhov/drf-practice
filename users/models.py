from pyexpat import model
from uuid import uuid4
from django.db import models

# TODO: Посолить пароль от греха подальше


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    login = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=60, null=False)
