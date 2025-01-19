from .models import Comment
from django import forms
from .models import CollaborateRequest


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)



#geza


class NewPostForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('title', 'slug', 'author', 'banner', 'content')
