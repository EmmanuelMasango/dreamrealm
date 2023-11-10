from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Album(models.Model):
    """
    Represents an album in the database.

    Attributes:
        title (str): The title of the album.
        release_date (Date): The release date of the album.
        genre (str): The genre of the album.
        description (str, optional): A description of the album (can be blank or null).
        spotify_link (URL): The Spotify link to the album.
        cover_image (ImageField): The cover image of the album.
        user (ForeignKey to User): The user who added this album to their collection.
    """
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    spotify_link = models.URLField()
    cover_image = models.ImageField(upload_to='albums/covers/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the album.
        """
        return self.title


class FavoriteAlbum(models.Model):
    """
    Represents a user's favorite album in the database.

    Attributes:
        user (ForeignKey to User): The user who marked this album as a favorite.
        album (ForeignKey to Album): The favorite album associated with the user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
