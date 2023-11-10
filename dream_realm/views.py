from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, FavoriteAlbum
from django.contrib.auth.decorators import login_required


def base_view(request):
    """
    Render the base view for the application's index page.

    Args:
       request (HttpRequest): The request object.

    Returns:
       HttpResponse: Rendered HTML response for the index page.
    """
    return render(request, 'dream_realm/index.html')


def album_list(request):
    """
    Render a list of albums, including information about whether they are in the user's favorites.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response for the album list page.
    """
    albums = Album.objects.all()
    user = request.user if request.user.is_authenticated else None
    for album in albums:
        album.is_favorite = FavoriteAlbum.objects.filter(user=user, album=album).exists()
    return render(request, 'dream_realm/albums.html', {'albums': albums})


def album_detail(request, album_id):
    """
    Render the details of a specific album, including whether it's in the user's favorites.

    Args:
        request (HttpRequest): The request object.
        album_id (int): The ID of the album to display.

    Returns:
        HttpResponse: Rendered HTML response for the album detail page.
    """

    album = get_object_or_404(Album, pk=album_id)
    is_favorite = False

    # Check if the user is authenticated before trying to access their favorite albums
    if request.user.is_authenticated:
        user = request.user
        # Check if this album is in the user's favorite albums
        is_favorite = FavoriteAlbum.objects.filter(user=user, album=album).exists()

    return render(request, 'dream_realm/album_detail.html', {'album': album, 'is_favorite': is_favorite})


@login_required
def add_favorite(request, album_id):
    """
    Add an album to the user's favorites.

    Args:
        request (HttpRequest): The request object.
        album_id (int): The ID of the album to add to favorites.

    Returns:
        HttpResponseRedirect: Redirects to the album list or a specific album detail page.
    """
    album = get_object_or_404(Album, pk=album_id)
    user = request.user

    # Check if the album is already marked as a favorite for the user
    favorite_exists = FavoriteAlbum.objects.filter(user=user, album=album).exists()

    if not favorite_exists:
        favorite = FavoriteAlbum(user=user, album=album)
        favorite.save()

    # Redirect back to the album list or a specific album detail page
    return redirect('dream_realm:album_list')  # Change 'album_list' to your desired URL name


@login_required
def remove_favorite(request, album_id):
    """
    Remove an album from the user's favorites.

    Args:
        request (HttpRequest): The request object.
        album_id (int): The ID of the album to remove from favorites.

    Returns:
        HttpResponseRedirect: Redirects to the album list or a specific album detail page.
    """
    album = get_object_or_404(Album, pk=album_id)
    user = request.user

    # Check if the album is marked as a favorite for the user
    favorite_exists = FavoriteAlbum.objects.filter(user=user, album=album).exists()

    if favorite_exists:
        favorite = FavoriteAlbum.objects.get(user=user, album=album)
        favorite.delete()

    # Redirect back to the album list or a specific album detail page
    return redirect('dream_realm:album_list')