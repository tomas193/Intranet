from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import FileExtensionValidator


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('posts')
    
class Video(models.Model):
    title=models.CharField(max_length=70)
    description=models.TextField()
    video_file=models.FileField(upload_to='uploads/video_files',validators=[FileExtensionValidator(allowed_extensions=['mp4','mov'])])
    thumbnail=models.FileField(upload_to='uploads/thumbnails',validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg'])])
    date_posted=models.DateTimeField(default=timezone.now)