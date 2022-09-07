from rest_framework.authtoken.models import Token
from dj_rest_auth.views import LoginView
from django.contrib.auth import login
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


class Users(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User_
    permission_classes = [AllowAny]


class Player_View(viewsets.ModelViewSet):
    """
      A viewset.ModelViewSet that provides default `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()`
       and `list()` actions
    """
    queryset = Prospect.objects.all()
    serializer_class = Player_Serializer_

    def list(self, request):
        queryset = self.get_queryset()
        serializer = Player_Serializer(queryset, many=True)
        return Response(serializer.data)


class Highschool_View(viewsets.ModelViewSet):
    queryset = HighSchool.objects.all()
    serializer_class = Heighschool_Serializer


class Team_View(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = Team_Serializer


class Position_View(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = Position_Serializer


class Country_View(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = Country_Serializer


class Year_View(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = Year_Serializer


class Offers_View(viewsets.ModelViewSet):
    queryset = Offers.objects.all()
    serializer = Offers_Serializer(queryset, many=True)
    serializer_class = Offers_Serializer


class City_View(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = City_Serializer_

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = City_Serializer(queryset, many=True)
        return Response(serializer.data)


class State_View(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = State_Serializer_

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = State_Serializer(queryset, many=True)
        return Response(serializer.data)


class HardCommited_View(viewsets.ModelViewSet):
    queryset = HardCommited.objects.all()
    serializer_class = HardCommited_Serializer_

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = HardCommited_Serializer(queryset, many=True)
        return Response(serializer.data)


class TwitterInfo_View(viewsets.ModelViewSet):
    queryset = TwitterInfo.objects.all()
    serializer_class = TwitterInfo_Serializer_

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TwitterInfo_Serializer(queryset, many=True)
        return Response(serializer.data)


class CustomAuthToken(LoginView):
    """ for dj-rest-auth we have return user id with token """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk
        })
