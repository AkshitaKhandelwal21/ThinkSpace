from django import forms

from blogs.models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter an eye-catching title'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a page heading'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Write your story...'
            })
        }