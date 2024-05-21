from django import forms
from .models import Post, Comment

class CommentForm(forms.ModelForm): # CommentForm 클래스 추가 

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)