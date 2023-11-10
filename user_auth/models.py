from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """
    Model representing a user profile.

    This model extends the built-in User model in Django to include additional user profile
    information, such as first name, last name, avatar, bio, date of birth, email, and new user status.

    Attributes:
        user (OneToOneField): A one-to-one relationship to the User model, linking the profile
            to a specific user.
        first_name (CharField): The first name of the user (maximum length: 30 characters).
        last_name (CharField): The last name of the user (maximum length: 30 characters).
        avatar (ImageField): An image representing the user's avatar.
        bio (TextField): A text field for the user's bio.
        date_of_birth (DateField): The user's date of birth.
        email (EmailField): The email address associated with the user.
        is_new (BooleanField): A boolean flag indicating if the user is new (default is True).

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    is_new = models.BooleanField(default=True)
