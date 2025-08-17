from django import forms
from .models import Post, Tag
from taggit.forms import TagWidget
from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
