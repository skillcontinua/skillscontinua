from django import forms
from.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_type','title','content','video_url','image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Catchy title...', 'class':'w-full p-3 border rounded-lg'}),
            'content': forms.Textarea(attrs={'rows':5, 'placeholder':'Share story, ask question, post job, reel link...', 'class':'w-full p-3 border rounded-lg'}),
            'video_url': forms.URLInput(attrs={'placeholder':'https://youtube.com/... (for Reel/Podcast)', 'class':'w-full p-3 border rounded-lg'}),
            'post_type': forms.Select(attrs={'class':'w-full p-3 border rounded-lg font-bold'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {'text': forms.TextInput(attrs={'placeholder':'Add a comment...', 'class':'w-full p-2 border rounded-full'})}