from django import forms
from .models import Comment, Post
from pagedown.widgets import AdminPagedownWidget


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)

	body = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Comment'}))
    

class PostForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget=AdminPagedownWidget())
    class Meta:
        model = Post
        fields = ('title', 'title_image', 'content', 'tags',)
