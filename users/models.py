from uuid import uuid4
from django.db import models
from django.contrib.auth import models as auth_models


class UserManager(auth_models.UserManager):
    def create_user(self, email: str, password: str, is_superuser=False, is_staff=False) -> "User":
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('User must have password')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.save()

        return user

    def create_superuser(self, email: str, password: str) -> "User":
        return self.create_user(email, password, is_superuser=True, is_staff=True)


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()
