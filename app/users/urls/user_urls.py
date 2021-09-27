from django.urls import path
from users.views.user_views import *

urlpatterns = [
    # CRUD => Create, Read, Update, Delete
    path('create', UserCreate.as_view()),#ok
    path('create/bulk', UserCreateBulk.as_view()),#ok
    path('create/bulk/jsondata', UserCreateBulk.as_view()),#ok
    path('list', UserList.as_view()),#ok
    path('get/<int:pk>', UserDetail.as_view()), #ok
    path('get/<employed_number>', UserDetailNestedEmployeds.as_view()), #ok
    path('update/<int:pk>', UserUpdate.as_view()),#ok
    path('delete/<int:pk>', UserDelete.as_view())#ok
]
