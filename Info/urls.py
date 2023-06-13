from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('register/',views.Register.as_view(),name='Register'),
    path('signin/',views.signin,name='Login'),
    path('signout/',views.signout,name='Logout'),
    path('activity/',views.check_activity,name='activity'),
]