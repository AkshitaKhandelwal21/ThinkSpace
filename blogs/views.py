from http.client import HTTPException
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from rest_framework import generics
from blogs.forms import CreatePostForm, UpdatePostForm
from blogs.models import Post
from comments.forms import CommentPostForm
from comments.models import Comment
from blogs.serilaizer import PostSerializer
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# class PostsList(TemplateView):
#     template_name = 'home.html'
#     # queryset = Post.objects.all()
#     # serializer_class = PostSerializer
#     try:
#         def get_context_data(self, **kwargs):
#             context = super().get_context_data(**kwargs)
#             context['posts'] = Post.objects.all()
#             return context
#     except Exception as e:
#         raise HTTPException(e)
    

class PostsList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class CreatePost(LoginRequiredMixin, CreateView):
#     form_class = CreatePostForm
#     model = Post
#     template_name = 'create_post.html'
#     success_url = reverse_lazy('all_posts')

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


class CreatePost(LoginRequiredMixin, generics.CreateAPIView):
    model = Post
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# class PostUpdate(LoginRequiredMixin, UpdateView):
#     model = Post
#     form_class = UpdatePostForm
#     template_name = 'update_post.html'

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_staff or user.is_superuser:
#             return Post.objects.all()
#         return Post.objects.filter(author=user)
    
#     def get_success_url(self):
#         return reverse('post_id', kwargs={'pk':self.kwargs['pk']})


class PostUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
    

# class PostDelete(LoginRequiredMixin, DeleteView):
#     model = Post
#     success_url = reverse_lazy('all_posts')

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_staff or user.is_superuser:
#             return Post.objects.all()
#         return Post.objects.filter(author=user) 

    # def get_success_url(self):
    #     return reverse('allblogs', kwargs={'pk':self.kwargs['pk']})


class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'   


# class OnePost(LoginRequiredMixin, DetailView):
#     model = Post
#     template_name = 'postId.html'
#     context_object_name = 'post'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = CommentPostForm()
#         context['comments'] = self.object.comments.filter(
#             is_approved=True).select_related('user')
#         return context


class OnePost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class OnePostComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentPostForm
    # template_name = 'postId.html'

    def get_success_url(self):
        return reverse('post_id', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.post = post
        return super().form_valid(form)
    

class PostsByUser(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)
    