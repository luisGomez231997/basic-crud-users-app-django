"""Imports"""
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from users.models.users import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    """CustomUserSerializer class"""
    
    class Meta:
        model = CustomUser
        fields =  [
            "name"
            "first_last_name"
            "second_last_name"
            "identity_document_number"
            "date_of_birth"
            "gender"
            "date_of_creation"
            "employed_number"
            "occupation"
            "boss"
            "zone"
            "municipe"
            "department"
            "sells"
            "email"
            "image"
            "cell_phone"
            "is_active"
            "is_staff"
            "is_superuser"
        ]        

    #class attributes:
        #empty

    #class methods:
    def create(self, validated_data):
        """Create a new object instance."""
        user_password = validated_data.pop('password')
        user = CustomUser.objects.create(password= make_password(user_password),**validated_data)
        user.username = validated_data['email']
        user.save()
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        user = super().update(instance, validated_data)
        return user
    
    def delete(self, instance):
        """delete a object instance."""
        user = CustomUser.objects.get(instance)
        user.delete()