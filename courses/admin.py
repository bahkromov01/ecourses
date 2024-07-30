from django.contrib import admin

from courses.models import Course, Comment, Category

# Register your models here.

admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(Category)