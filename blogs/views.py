from http.client import HTTPException
from django.shortcuts import render
from rest_framework import generics
from blogs.models import Post
from blogs.serilaizer import PostSerializer
from django.views.generic import TemplateView

# Create your views here.
class PostsList(TemplateView):
    template_name = 'home.html'
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer

    # def post(self, request):
    #     breakpoint()
    #     return None

    try:

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['posts'] = Post.objects.all()
            return context
    except Exception as e:
        raise HTTPException(e)
    

class CreatePost(generics.CreateAPIView):
    model = Post
    serializer_class = PostSerializer