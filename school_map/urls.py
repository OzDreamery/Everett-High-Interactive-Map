from django.urls import path
from .views import room_input
from django.contrib.auth import views as auth_views

from . import views

app_name = 'school_map'
urlpatterns = [
  
    path('', views.authentication, name='authentication'),
    path('floor1/', views.floor1, name='floor1'),
    path('floor2/', views.floor2, name='floor2'),
    path('floor3/', views.floor3, name='floor3'),
    path('floor4/', views.floor4, name='floor4'),
    path('floor5/', views.floor5, name='floor5'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('room_input/', views.room_input, name='RoomInput'),
    path('room_input/', room_input, name='room_input'),
]
