from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Teachers, Comment

admin.site.register(Teachers)
admin.site.register(Comment)
