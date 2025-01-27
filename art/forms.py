from .models import Comment
from django import forms
#from .models import CollaborateRequest
from .models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)



#geza add New Post Form


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'banner', 'content','status','excerpt',)
