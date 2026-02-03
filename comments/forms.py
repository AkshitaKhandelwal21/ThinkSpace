from django import forms
from .models import Comment

class CommentPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form_control'
            })
        }
        