from django import forms
from .models import Post, Reply


class PostForm(forms.ModelForm):
    """
    Form for creating or updating a post.

    This form is used to create or edit a post, allowing users to input a title
    and content for the post.

    Attributes:
       model (Post): The model associated with this form.
       fields (list): The fields to include in the form, which are 'title' and 'content'.

    """
    class Meta:
        model = Post
        fields = ['title', 'content']


class ReplyForm(forms.ModelForm):
    """
    Form for creating or updating a post.

    This form is used to create or edit a post, allowing users to input a title
    and content for the post.

    Attributes:
       model (Post): The model associated with this form.
       fields (list): The fields to include in the form, which are 'title' and 'content'.

    """
    class Meta:
        model = Reply
        fields = ['content']
