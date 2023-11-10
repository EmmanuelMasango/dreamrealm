from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'dream_realm'

# URL patterns for the 'dream_realm' app.
urlpatterns = [
    path("", views.base_view, name="index"),
    path('albums/', views.album_list, name='album_list'),
    path('albums/<int:album_id>/', views.album_detail, name='album_detail'),
    path('add_favorite/<int:album_id>/', views.add_favorite, name='add_favorite'),
    path('remove_favorite/<int:album_id>/', views.remove_favorite, name='remove_favorite'),
]

# If in DEBUG mode, serve media files (e.g., images) during development.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
