# Register your models here.

from django.contrib import admin
from .models import Post, Comment # Comment 추가 

admin.site.register(Post)
admin.site.register(Comment) # 추가 