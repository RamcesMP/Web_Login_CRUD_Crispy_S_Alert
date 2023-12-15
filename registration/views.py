from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


class UserCreateView(CreateView):
    form_class=UserCreationForm
    template_name='registration/registro.html'
    success_url=reverse_lazy('home')


