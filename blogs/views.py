from http.client import HTTPException
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from rest_framework import generics
from blogs.forms import CreatePostForm, UpdatePostForm
from blogs.models import Post
from blogs.paginations import CustomPagination, MyCursorPagination
from comments.forms import CommentPostForm
from comments.models import Comment
from blogs.serilaizer import CommentSerializer, PostSerializer
from django.views.generic import *
from rest_framework.generics import *
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



# class CreatePost(LoginRequiredMixin, CreateView):
#     form_class = CreatePostForm
#     model = Post
#     template_name = 'create_post.html'
#     success_url = reverse_lazy('all_posts')

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)



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


    



# ********************************** Blogs with DRF *************************************

class BlogsView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # pagination_class = CustomPagination
    pagination_class = MyCursorPagination


class CommentsView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BlogsViewById(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


class CommentsViewById(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'