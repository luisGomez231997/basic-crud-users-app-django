from django.urls import path
from oauth.views.login_views import *

urlpatterns = [
    # access_point uris => access to auth info..
    path('login', LogIn.as_view()), #ok
]
