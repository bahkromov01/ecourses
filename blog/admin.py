from django.contrib import admin

from blog.models import Blog, Author, Image, Comment

# Register your models here.

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Image)
admin.site.register(Comment)

