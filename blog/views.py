from django.shortcuts import render
from django.views import View

from blog.models import Blog, Comment, Author


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

# def blog(request):
#     return render(request, 'blog/blog.html')


class BlogPage(View):
    def get(self, request):
        blogs = Blog.objects.all()
        authors = Author.objects.all()

        context = {

            'blogs': blogs,
            'active_page': 'blog',
            'authors': authors
        }
        return render(request, 'blog/blog.html', context)


class AuthorPage(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'blog/blog.html', {'authors': authors})


class BlogDetail(View):
    def get(self, request):
        return render(request, 'blog/blog_detail.html')


class CommentPage(View):
    def get(self, request):
        comments = Comment.objects.all()

        context = {
            'comments': comments
        }
        return render(request, 'blog/blog.html', context)


