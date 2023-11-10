from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Reply
from .forms import PostForm, ReplyForm
from django.contrib.auth.decorators import login_required


def forum_home(request):
    """
    Display the forum home page with a list of posts.

    This view retrieves all posts ordered by their creation date and renders
    them on the forum home page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The forum home page with a list of posts.
    """
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'realm_forum/forum_home.html', {'posts': posts})


def view_post(request, post_id):
    """
    Display a specific post along with its replies.

    This view retrieves a specific post and its associated replies, then renders
    them on the view post page.

    Args:
        request (HttpRequest): The request object.
        post_id (int): The ID of the post to view.

    Returns:
        HttpResponse: The view post page displaying the post and replies.
    """
    post = get_object_or_404(Post, pk=post_id)
    replies = Reply.objects.filter(post=post).order_by('created_at')
    return render(request, 'realm_forum/view_post.html', {'post': post, 'replies': replies})


@login_required
def create_post(request):
    """
    Create a new post.

    This view handles the creation of a new post. If the request method is POST
    and the form is valid, a new post is created.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The create post page or a redirect to the forum home page.
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('realm_forum:forum_home')
    else:
        form = PostForm()
    return render(request, 'realm_forum/create_post.html', {'form': form})


@login_required
def create_reply(request, post_id):
    """
    Create a new reply to a post.

    This view handles the creation of a new reply to a specific post. If the request
    method is POST and the form is valid, a new reply is created.

    Args:
        request (HttpRequest): The request object.
        post_id (int): The ID of the post to which the reply is created.

    Returns:
        HttpResponse: The create reply page or a redirect to the view post page.
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.post = post
            reply.save()
            return redirect('realm_forum:view_post', post_id=post_id)
    else:
        form = ReplyForm()
    return render(request, 'realm_forum/create_reply.html', {'form': form})


@login_required
def upvote_reply(request, reply_id):
    """
        Upvote or unupvote a reply.

        This view allows users to upvote or unupvote a reply. It checks if the user
        has already upvoted the reply and updates the upvotes accordingly.

        Args:
            request (HttpRequest): The request object.
            reply_id (int): The ID of the reply to upvote or unupvote.

        Returns:
            HttpResponse: A redirect to the view post page containing the upvoted reply.
    """
    reply = get_object_or_404(Reply, pk=reply_id)

    if request.user not in reply.upvotes.all():
        reply.upvotes.add(request.user)
    else:
        reply.upvotes.remove(request.user)

    return redirect('realm_forum:view_post', post_id=reply.post.id)
