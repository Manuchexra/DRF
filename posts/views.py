from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.

class PostListView(ListView):
    model=Post
    template_name='list.html'
    context_object_name='posts'

class PostDetailView(DetailView):
    model=Post
    template_name='detail.html'
    context_object_name='post'
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    template_name='create.html'

    fields=['title','body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy("posts:detail", kwargs={'pk':self.object.pk})
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model=Post
    template_name='update.html'
    context_object_name='post'

    fields=['title', 'body']

    def test_func(self):
        post=self.get_object()
        user=self.request.user

        if user== post.author:
            return True
        else:
            return False
    
    def get_success_url(self) -> str:
        return reverse_lazy("posts:detail", kwargs={'pk':self.object.pk})
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model=Post
    template_name='delete.html'
    context_object_name='post'
    success_url="/"

    def test_func(self):
        post=self.get_object()
        user=self.request.user

        if user== post.author:
            return True
        else:
            return False