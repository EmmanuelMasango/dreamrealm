from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    """
    Represents a post created by a user.

    This model represents a post, which includes the user who created the post,
    a title, the content of the post, and the date and time it was created.

    Attributes:
        user (User): The user who created the post.
        title (str): The title of the post (limited to 200 characters).
        content (str): The content of the post.
        created_at (datetime): The date and time when the post was created.

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


class Reply(models.Model):
    """
    Represents a reply to a post.

    This model represents a reply to a post. It includes the user who posted
    the reply, the post to which the reply is associated, the content of the
    reply, the date and time it was created, and any upvotes received.

    Attributes:
        user (User): The user who posted the reply.
        post (Post): The post to which the reply is associated.
        content (str): The content of the reply.
        created_at (datetime): The date and time when the reply was created.
        upvotes (ManyToManyField): Users who have upvoted this reply.

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    upvotes = models.ManyToManyField(User, related_name='upvoted_replies', blank=True)

