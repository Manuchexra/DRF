from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView
# Create your views here.

class PostListView(ListView):
    model=Post
    template_name='list.html'
    context_object_name='posts'