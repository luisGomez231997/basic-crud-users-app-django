"""Imports""" 
#python libs.
import datetime
#django libs.
from django.db import models
from django.contrib.auth.models import AbstractUser
#local packages.
from commons.oauth.oauth_manager import UserManager

class CustomUser(AbstractUser):
    """Custom User class: it is an object than represent a base model a user into the app."""
    #Class attributes.
    class Meta:
        """Meta class: allow modify the meta information in the Database, as a table name."""
        db_table = "CustomUser"
    username = None
    first_name = None
    last_name = None

    GENDER = (
        ("M", "MALE"),
        ("F", "FAMALE")
    )

    #Databases fields
    name = models.CharField(max_length=100, null=False)
    first_last_name = models.CharField(max_length=100, null=False)
    second_last_name = models.CharField(max_length=100, null=True)
    identity_document_number = models.IntegerField()
    date_of_birth = models.DateField(default=datetime.date.today, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default="M")
    date_of_creation = models.DateField(auto_now_add=True)
    employed_number = models.IntegerField()
    occupation = models.CharField(max_length=100)
    boss = models.IntegerField()
    zone = models.CharField(max_length=100)
    municipe = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    sells = models.IntegerField()
    email = models.EmailField(max_length=100, null=False, unique=True)
    image = models.CharField(max_length=1000, null=True, blank=True)
    cell_phone = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Configuration fields.
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]