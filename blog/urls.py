from django.urls import path

from main.views import index
from . import views
from .views import blog, blog_detail

urlpatterns = [
    path('index/', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog_detail/', blog_detail, name='blog_detail'),
]
