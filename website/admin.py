from django.contrib import admin
from .models import Post
from .models import Video

admin.site.register(Video)
admin.site.register(Post)
