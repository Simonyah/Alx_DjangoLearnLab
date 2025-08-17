from django import forms
from .models import Post, Tag
from taggit.forms import TagWidget
from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include tags
        widgets = {
            'tags': TagWidget(),  # This makes the tags input work correctly
        }

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
