from django.contrib import admin
from .models import Image, Post, Profile


admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Profile)
