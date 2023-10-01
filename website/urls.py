from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView,PostDeleteView,CreateVideo,DetailVideo

urlpatterns = [
    path('', views.home, name='web-home'),
    #path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),
    path('streaming/', views.streaming, name='streaming'),
    path('upload/', CreateVideo.as_view(), name='video-upload'),
    path('videtail/<int:pk>/', DetailVideo.as_view(), name='video-detail'),
] 
   