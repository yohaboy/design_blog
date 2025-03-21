from django.views.generic import View,CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import User
from .forms import RegisterForm


class RegsiterUser(CreateView):
    model = User
    template_name = 'accounts/login-register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request , user)

        return redirect(self.success_url)
    
class LoginUser(LoginView):
    template_name = 'accounts/login-register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

class LogoutUser(LogoutView):
    next_page = reverse_lazy('home')