from django.shortcuts import render,HttpResponse
from django.contrib.auth.views import LoginView,TemplateView
from django.views.generic import CreateView
from .models import Account
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
'''
class LoginPageView(LoginView):
    template_name = ''
'''
class UserCreationView(CreateView):
    model = Account
    fields= ('first_name','last_name','cnic','email','phone','address','city','country')

@method_decorator(login_required,name='dispatch')
class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'