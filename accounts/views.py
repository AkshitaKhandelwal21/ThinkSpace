from urllib import response
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView
from rest_framework import generics
from django.contrib.auth import authenticate, login
from accounts.forms import LoginForm, RegisterForm
from accounts.models import User
from accounts.serializers import RegisterSerializer
from blogs.models import Post

# Create your views here.
# class HomeView(TemplateView):
#     template_name = 'home.html'

class Register(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

   
class Login(FormView):  
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        print(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request=self.request, username=username, password=password)
        print(user)
        if user is None:
            return redirect('/users/login')
        else:
            login(self.request, user)
            return redirect('/allblogs')
        