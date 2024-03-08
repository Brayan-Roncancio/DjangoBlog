from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .forms import *
from .models import Post

class BlogListView(ListView):
    model=Post
    template_name='home.html'
    ordering = ['-id']

class BlogDetailView(DetailView):
    model=Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_new.html'
    #fields=['title','author','body']
    
class BlogEditView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'post_update.html'
    #fields=['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

# Create your views here.
