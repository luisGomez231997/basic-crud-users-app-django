"""Imports"""
#django libs.
from django.contrib.auth.models import (BaseUserManager)
from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    """UserManager class: it is a object than connect the default
     user model of django with a custom user instance."""

     #Class Attributes: ---------------------------------------------------
        # empty

     #Class Methods: -------------------------------------------------------
    def __init__(self) -> None:
         """Constructor class."""
         #instance attributes.
         super().__init__()

    def create_user(self, email, password, **extra_fields):
        """"create_user method: create and save a new user"""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, **extra_fields):
        """create_staffuser method: create and save a new staffuser"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        user = self.create_user(email, password, **extra_fields)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """"create_superuser method: create and save a new super user"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user = self.create_user(email, password, **extra_fields)
        return user

    def create_token(user):
        """create token access to user"""
        token, create = Token.objects.get_or_create(user=user)
        return token.key

    def get_user_by_token(token_key):
        """get the user by token key"""
        try:
            token = Token.objects.get(key=token_key)
            return token.user_id
        except:
            return None