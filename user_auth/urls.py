from django.urls import path
from django.utils.deprecation import MiddlewareMixin

from . import views

app_name = 'user_auth'

# URLS for user_auth app
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('show_user/', views.show_user, name='show_user'),
    path('user/', views.show_user, name='user'),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]



