from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
#add Geza
from django.urls import path 
from . import views
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .models import CollaborateRequest 
from .forms import NewPostForm

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "art/index.html"
    paginate_by = 6


def post_detail(request, slug):
    
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    
    comment_form = CommentForm()

    return render(
        request,
        "art/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "coder": "Geza Csosz",
            "comment_count": comment_count,
            "comment_form": comment_form
        },
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# Geza

#@permission_required('art.can_view_mymodel')
#def my_view(request):
    # Your view logic here
    #return render(request, 'art/my_template.html')

# Geza add  login to the post_new.html
#@login_required(login_url="login/")
#def post_new(request):
    #return render(request, 'art/post_new.html')
#new one


def group_required(group_name="default"):
    def in_groups(user):
        return user.is_authenticated and user.groups.filter(name=group_name).exists()
    return user_passes_test(in_groups)

# Apply the decorator to your view


@login_required 

def post_list_view(request):
     if request.method == "POST":
         form = NewPostForm(request.POST, request.FILES)
         if form.is_valid():
            post = form.save(commit=False)  # Don't save to the database yet
            post.author = request.user      # Set the author to the logged-in user
            post.save()                      # Now save the post
            return redirect('post_list_view')
     else:
         form = NewPostForm()
     posts = Post.objects.all()
     return render(request, 'art/post_list.html', {'posts': posts, 'form': form})

     #new
     