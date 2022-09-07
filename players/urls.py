from django.urls import path, include
from .views import *

app_name = 'players'
Profile_list = Player_View.as_view({'get': 'list', 'post': 'create', })
Profile_detail = Player_View.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy', })

school_list = Highschool_View.as_view({'get': 'list', 'post': 'create', })
school_detail = Highschool_View.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy', })

position_list = Position_View.as_view({'get': 'list', 'post': 'create', })
position_detail = Position_View.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy', })

city_list = City_View.as_view({'get': 'list', 'post': 'create', })
city_detail = City_View.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy', })

state_list = State_View.as_view({'get': 'list', 'post': 'create', })
state_detail = State_View.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy', })

country_list = Country_View.as_view({'get': 'list', 'post': 'create', })
country_detail = Country_View.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy', })

offers_list = Offers_View.as_view({'get': 'list', 'post': 'create', })
offers_detail = Offers_View.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy', })

team_list = Team_View.as_view({'get': 'list', 'post': 'create', })
team_detail = Team_View.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy', })

year_list = Year_View.as_view({'get': 'list', 'post': 'create', })
year_detail = Year_View.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy', })

commited_list = HardCommited_View.as_view({'get': 'list', 'post': 'create', })
commited_detail = HardCommited_View.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy', })

twitter_list = TwitterInfo_View.as_view({'get': 'list', 'post': 'create', })
twitter_detail = TwitterInfo_View.as_view(
    {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy', })

urlpatterns = [
    path('profile/', Profile_list, name='profile_list'),
    path('profile/<int:pk>/', Profile_detail, name='profile_detail'),
    path('user/', Users.as_view(), name='createuser'),
    path('position/', position_list, name='position_list'),
    path('position/<int:pk>/', position_detail, name='position_detail'),
    path('country/', country_list, name='country_list'),
    path('country/<int:pk>/', country_detail, name='country_detail'),
    path('state/', state_list, name='state_list'),
    path('state/<int:pk>/', state_detail, name='state_detail'),
    path('city/', city_list, name='city_list'),
    path('city/<int:pk>/', city_detail, name='city_detail'),
    path('school/', school_list, name='school_list'),
    path('school/<int:pk>/', school_detail, name='school_detail'),
    path('twitter/', twitter_list, name='twitter_list'),
    path('twitter/<int:pk>/', twitter_detail, name='twitter_detail'),
    path('commited/', commited_list, name='commited_list'),
    path('commited/<int:pk>/', commited_detail, name='commited_detail'),
    path('year/', year_list, name='year_list'),
    path('year/<int:pk>/', year_detail, name='year_detail'),
    path('offer/', offers_list, name='offer_list'),
    path('offer/<int:pk>/', offers_detail, name='offer_detail'),
    path('team/', team_list, name='team_list'),
    path('team/<int:pk>/', team_detail, name='team_detail'),
    path('login/', CustomAuthToken.as_view(), name='login_user'),
    path('dj-rest-auth/logout/', include('dj_rest_auth.urls')),
]
