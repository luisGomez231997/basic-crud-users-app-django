"""Imports"""
# drf libs.
from rest_framework import status
from rest_framework.generics import CreateAPIView
# local packages.
from users.controllers.user_controller import CustomUser
from oauth.serializers.login_serializer import (LoginSerializer, ApiRestUtilities)

class LogIn(CreateAPIView):
    """LogIn End-Point(Post):  the endpoint receive a user gmail and password,
     and return the user object and the token access."""

    # Class attributes:
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):
        """Http post metod"""
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'profile': user,
            'token': token
        }
        return ApiRestUtilities.get_rest_successfull_response(
            "Login successful.", data, status.HTTP_200_OK)
