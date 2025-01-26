from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Post, Comment
from .forms import CommentForm, NewPostForm

# Search functionality integrated into PostList view
class PostList(generic.ListView):
    template_name = "art/index.html"
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            result = Post.objects.filter(status=1).filter(
                title__icontains=query
            ) | Post.objects.filter(
                excerpt__icontains=query
            )
            if not result.exists():
                messages.info(self.request, "I did not find any content that matched my search in the content and titles of the articles.")
            return result
        return Post.objects.filter(status=1)

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
            messages.success(request, 'Comment submitted and awaiting approval')
    else:
        comment_form = CommentForm()
    
    return render(request, "art/post_detail.html", {
        "post": post,
        "comments": comments,
        "coder": "Geza Csosz",
        "comment_count": comment_count,
        "comment_form": comment_form
    })

def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        post = get_object_or_404(Post, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment Updated!')
        else:
            messages.error(request, 'Error updating comment!')
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

@login_required
def post_list_view(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(excerpt__icontains=query)
        if not posts.exists():
            messages.info(request, "I did not find any content that matched my search in the content and titles of the articles.")
    else:
        posts = Post.objects.all()
    
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list_view')
    else:
        form = NewPostForm()
    
    return render(request, 'art/post_list.html', {'posts': posts, 'form': form, 'form_style': 'max-width: 300px; float: left;', 'button_color': '#f4ffc3'})
