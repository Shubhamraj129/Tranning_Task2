from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class User_(serializers.ModelSerializer):
    @staticmethod
    def validate_password(password: str) -> str:
        """
            PASSWORD(str) calculates and returns a password string from the plaintext password str and returns a binary
             string.
        """
        return make_password(password)

    class Meta:
        model = User
        fields = '__all__'


class Player_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Prospect
        depth = 2
        fields = '__all__'


class Player_Serializer_(serializers.ModelSerializer):
    class Meta:
        model = Prospect
        fields = '__all__'


class Heighschool_Serializer(serializers.ModelSerializer):
    class Meta:
        model = HighSchool
        fields = '__all__'


class Position_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class City_Serializer(serializers.ModelSerializer):
    class Meta:
        model = City
        depth = 3
        fields = '__all__'


class City_Serializer_(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class Team_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class State_Serializer(serializers.ModelSerializer):
    class Meta:
        model = State
        depth = 1
        fields = '__all__'


class State_Serializer_(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class TwitterInfo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterInfo
        depth = 3
        fields = '__all__'


class TwitterInfo_Serializer_(serializers.ModelSerializer):
    class Meta:
        model = TwitterInfo
        fields = '__all__'


class HardCommited_Serializer(serializers.ModelSerializer):
    class Meta:
        model = HardCommited
        depth = 3
        fields = '__all__'


class HardCommited_Serializer_(serializers.ModelSerializer):
    class Meta:
        model = HardCommited
        fields = '__all__'


class Country_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class Offers_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = '__all__'


class Year_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'
