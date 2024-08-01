from django.contrib import admin

# Register your models here.

from .models import BlogAuthor, Blog_list, BlogComment, BlogImage

admin.site.register(BlogAuthor)
admin.site.register(BlogComment)


class BlogCommentsInline(admin.TabularInline):
    model = BlogComment
    max_num = 0

@admin.register(Blog_list)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date')
    inlines = [BlogCommentsInline]

@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    list_display = ('blog_id',)