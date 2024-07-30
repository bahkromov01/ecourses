from django.shortcuts import render
from django.views import View


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

# def blog(request):
#     return render(request, 'blog/blog.html')

class BlogPage(View):
    def get(self, request):
        return render(request,'blog/blog.html')



def blog_detail(request):
    return render(request, 'blog/blog_detail.html')


