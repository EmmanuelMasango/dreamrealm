from django.urls import path
from . import views

app_name = 'realm_forum'

# URL Patterns for realm_forum app
urlpatterns = [
    path('', views.forum_home, name='forum_home'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/reply/', views.create_reply, name='create_reply'),
    path('reply/upvote/<int:reply_id>/', views.upvote_reply, name='upvote_reply'),
]
