from django.urls import path

from blogs import views

urlpatterns = [
    path('allblogs', views.PostsList.as_view()),
    path('newblog', views.CreatePost.as_view()),
]
