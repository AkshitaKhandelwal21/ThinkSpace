from django.urls import path

from accounts import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
]