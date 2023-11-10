from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .forms import UserRegistrationForm, ProfileForm
from django.http import Http404
from .models import Profile


def user_login(request):
    """
    Renders the login template.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered login template.
    """

    return render(request, 'authentication/login.html')


def authenticate_user(request):
    """
    Authenticate user details.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponseRedirect: Redirects to the login page on failure, or the user's profile on success.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponseRedirect(
                reverse('user_auth:login')
            )
        else:
            login(request, user)
            return HttpResponseRedirect(
                reverse('user_auth:show_user')
                )
    return render(request, 'authentication/login.html')


def user_logout(request):
    """
    Log the user out and redirect to the home page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Redirects to the home page.
    """
    logout(request)
    return redirect('dream_realm:index')


def register(request):
    """
    Renders the registration form and handles user registration.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders the registration form or redirects to the user's profile page on successful registration.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a user profile associated with the user
            profile = Profile(user=user)
            profile.is_new = True  # Assuming all new profiles are marked as new
            profile.first_name = ""  # Default value for first_name
            profile.last_name = ""  # Default value for last_name
            profile.email = ""  # Default value for email
            profile.date_of_birth = None  # Default value for date_of_birth (None if not provided)

            # To set a default avatar, you can use the path you mentioned
            profile.avatar = 'user_auth/static/default_image.jpg'

            # Optionally, set some initial data for the profile
            profile.bio = "Write something about yourself"
            profile.save()

            # Log the user in after registration if needed
            login(request, user)
            return redirect('user_auth:show_user')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})


@login_required
def edit_profile(request):
    """
    Edit the user's profile information.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders the profile edit form or redirects to the user's profile page on successful edit.
    """
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user.profile, files=request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.is_new = False
            profile.save()
            return redirect('user_auth:show_user')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile/edit_profile.html', {'form': form})


@login_required
def show_user(request):
    """
    Display the user's profile.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders the user's profile page.
    """
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # If the profile doesn't exist, create a new one
        profile = Profile.objects.create(user=request.user)
        # You can also set default values for fields here, e.g., profile.is_new = True

    return render(request, 'authentication/user.html', {'profile': profile})
