"""Imports"""
# django libs.
from django.contrib.auth import authenticate
# drf libs.
from rest_framework import serializers
# local packages.
from commons.oauth.oauth_manager import UserManager
from commons.utils.server.rest_utils import ApiRestUtilities

class LoginSerializer(serializers.Serializer):
    """LoginSerializer class: is a parser class that manage the transactional operations
       corresponding to the login process"""

    # Class attributes:
    email = serializers.EmailField()
    password = serializers.RegexField(regex="", min_length=8, max_length=64)

    # Class Methods:
    def __init__(self, instance, data, **kwargs):
        """Constructor class"""
        # Instance attributes:
        super().__init__(instance=instance, data=data, **kwargs)

    def validate(self, data) -> None:
        """Validate: consult the db for a user with this credencials,
           if not exist get a status code 400 rest response.
           Else get a user object."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            ApiRestUtilities.get_rest__validation_error_response(
                'The credencials is not valid.', "email", 400)
        self.context['user'] = user
        return data

    def create(self, data)-> any:
        """Return the object data and the token acceess."""
        if self.validate(data) is None:
            return None 
        user = self.context['user']
        return user, UserManager.create_token(user)