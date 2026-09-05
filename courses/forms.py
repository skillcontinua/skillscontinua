from django import forms
from .models import Lesson, Course

class LessonUploadForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content_type', 'order', 'youtube_url', 'video_file', 'audio_file', 'pdf_file', 'content', 'is_free_preview']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. How to dismantle Carburetor'}),
            'content': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'youtube_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://youtube.com/... (saves server space)'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'video_file': 'VIDEO = Practical demo (How to dismantle Carburetor, How to wire Flywheel) - MP4',
            'audio_file': 'AUDIO = Theory + Igbo explanation for low-data Aba students - MP3',
            'pdf_file': 'PDF = Manuals, wiring diagrams, safety sheets for offline',
            'content_type': 'Choose type - determines which file type to show',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(is_active=True)
        self.fields['course'].widget.attrs.update({'class': 'form-control'})
        self.fields['content_type'].widget.attrs.update({'class': 'form-control'})