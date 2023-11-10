from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    """
    A form for user registration.

    This form allows users to register with their first name and user credentials.
    It extends the built-in User model in Django.

    Attributes:
        first_name (CharField): A text field for the user's first name.

    Methods:
        save: Save the user registration information and create a new user instance.

    """
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password1', 'password2']

    def save(self, commit=True):
        """
        Save the user registration information and create a new user instance.

        This method is used to save the user's registration information and create a new user
        instance. It sets the first name for the user based on the input in the form. By default,
        the method will save the user instance, but this can be controlled with the `commit`
        parameter.

        Args:
            commit (bool, optional): If True, the user instance is saved to the database.
                If False, it is not saved (default is True).

        Returns:
            User: The user instance created or updated.

        """
        user = super(UserRegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    """
    A form for updating user profile information.

    This form allows users to edit their profile information, including first name, last name,
    avatar, bio, date of birth, and email. It includes validation to ensure the email address is
    unique among users.

    Attributes:
       bio (CharField): A text field for the user's bio.

    Meta:
       model (Profile): The model associated with the form.
       fields (list): The fields to include in the form.

    Methods:
       clean: Custom form validation to check the uniqueness of the email address.

    """
    bio = forms.CharField(max_length=300, required=False, widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'avatar', 'bio', 'date_of_birth', 'email']

    def clean(self):
        """
        Custom form validation to check the uniqueness of the email address.

        This method validates that the email address provided in the form is unique among users.
        It checks if the email is already in use by a different user.

        Raises:
            forms.ValidationError: If the email address is already in use.

        """
        cleaned_data = super().clean()
        email = cleaned_data.get('email', None)
        user = self.instance.user  # Get the user associated with the profile

        # If the email is provided and different from the user's email, check if it's unique
        if email and email != user.email:
            if User.objects.filter(email=email).exclude(username=user.username).exists():
                raise forms.ValidationError('Email address is already in use.')
