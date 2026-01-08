from django.urls import path

from blogs import views

urlpatterns = [
    path('allblogs/', views.PostsList.as_view(), name='all_posts'),
    path('newblog/', views.CreatePost.as_view(), name='create_post'),
    path('post/<int:pk>/', views.OnePost.as_view(), name='post_id'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='delete_post'),
    path('post/<int:pk>/comment/', views.OnePostComment.as_view(), name='comment')
]
