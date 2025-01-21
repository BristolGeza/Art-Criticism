from .models import Comment
from django import forms
from .models import CollaborateRequest
from .models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)



#geza


class NewPostForm(forms.ModelForm):
    class Meta:
       # model = CollaborateRequest
        model = Post
        fields = ('title', 'slug', 'author', 'banner', 'content','status','excerpt')
