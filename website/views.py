from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,reverse
from .models import Post, Video
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView as cv2
from django.views.generic.detail import DetailView as dv2

@login_required
def home(request):
    return render(request,'website/home.html',{'title':'Home'})

@login_required
def post(request):
    context={
        'posts':Post.objects.all(),
        'title':'Posts'
    }
    return render(request,'website/post.html',context)


class PostListView(LoginRequiredMixin, ListView):
    model=Post
    template_name='website/post.html'
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post 
    success_url='/posts/'

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

@login_required
def about(request):
    return render(request,'website/about.html',{'title':'About'})

@login_required
def streaming(request):
    return render(request,'website/streaming.html',{'title':'Media Content'})

class CreateVideo(cv2):
    model=Video
    fields=['title','description','video_file','thumbnail']
    template_name='website/create_video.html'

    def get_success_url(self):
        return reverse('video-detail',kwargs={'pk':self.object.pk})

class DetailVideo(dv2):
    model=Video
    template_name='website/video_detail.html'