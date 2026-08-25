from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_type','title','content','video_url']
        widgets = {
            'content': forms.Textarea(attrs={'rows':5, 'placeholder':'Share your story, question, or achievement...'}),
            'title': forms.TextInput(attrs={'placeholder':'Title'}),
        }