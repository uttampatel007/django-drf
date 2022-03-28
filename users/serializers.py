from .models import UserData
from rest_framework import serializers


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = [
            "first_name",
            "last_name",
            "email",
            "age",
            "address",
        ]

