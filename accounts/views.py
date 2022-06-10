from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.


class LogIn(LoginView):
    template_name = 'login.html'
    success_url = '/'
