from http.client import HTTPException
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework import generics
from blogs.forms import CreatePostForm
from blogs.models import Post
from blogs.serilaizer import PostSerializer
from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PostsList(TemplateView):
    template_name = 'home.html'
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer
    try:
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['posts'] = Post.objects.all()
            return context
    except Exception as e:
        raise HTTPException(e)
    

class OnePost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'postId.html'


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = CreatePostForm
    model = Post
    template_name = 'create_post.html'
    success_url = reverse_lazy('all_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
