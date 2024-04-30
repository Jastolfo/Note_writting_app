from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User

    # Data fields for serialized User
    fields = ["id", "username", "password"]

    # Requirement to restrict password to only be view if written password sent to backend
    extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
      user = User.objects.create_user(**validated_data)
      return user
  
  def validate_password(self, value:str) -> str:
    """
    Hash value passed by user.

    :param value: password of a user
    :return: a hashed version of the password
    """
    return make_password(value)

class NoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Note
    fields = ["id", "title", "content", "created_at", "author"]

    # Author data should only be viewed and not edited
    extra_kwargs = {"author" : {"read_only": True}}

    