from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DetailView
# Create your views here.

class PostListView(ListView):
    model=Post
    template_name='list.html'
    context_object_name='posts'

class PostDetailView(DetailView):
    model=Post
    template_name='detail.html'
    context_object_name='post'