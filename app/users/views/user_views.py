# Imports
from rest_framework.generics import (
    CreateAPIView,  # create one
    RetrieveAPIView,  # get one (filter)
    ListAPIView,  # get all (filter)
    RetrieveUpdateAPIView,  # update one
    DestroyAPIView,  # delete one
)
from users.controllers.user_controller import (
    CustomUser, CustomUserSerializer, UserController)
from commons.utils.server.rest_utils import ApiRestUtilities

class UserCreate(CreateAPIView):
    """View to Create Users"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserCreateBulk(CreateAPIView):
    """View to create bulk users"""

    def post(self, request):
        user_controller = UserController()
        user_controller.create_bulk(request.data)
        if isinstance(user_controller, str):
            ApiRestUtilities.get_rest__validation_error_response(
                user_controller, "Users", 400)
        return ApiRestUtilities.get_rest_successfull_response("Creation Bulk Successful.", {}, 200)

class UserLoadJsonUserBulk(CreateAPIView):
    """View to create bulk users"""

    def post(self, request):
        user_controller = UserController()
        user_controller.load_json_users(request.data)
        if isinstance(user_controller, str):
            ApiRestUtilities.get_rest__validation_error_response(
                user_controller, "Users", 400)
        return ApiRestUtilities.get_rest_successfull_response("Creation Bulk Successful.", {}, 200)


class UserDetail(RetrieveAPIView):
    """View to Retrive a Users and acumulated sells by employes"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserDetailNestedEmployeds(RetrieveAPIView):
    """View to Retrive a Users"""
    lookup_field = "employed_number"

    def get(self, request, *args, **kwargs):
        try:
            employed_number: int = kwargs['employed_number']
            controller = UserController()
            data = controller.get_employed_info(employed_number)
            return ApiRestUtilities.get_rest_successfull_response("User retrive Successful.",
                                                                  data, 200)
        except:
            ApiRestUtilities.get_rest__validation_error_response(
                "The employed_number is a invalid code.", "employed_number", 400)


class UserList(ListAPIView):
    """View to List a Users"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserUpdate(RetrieveUpdateAPIView):
    """View to Update a Users"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserDelete(DestroyAPIView):
    """View to Delete a Users"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
