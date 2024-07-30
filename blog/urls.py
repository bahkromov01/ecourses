from django.urls import path

from main.views import index
from . import views
from .views import blog_detail, BlogPage
urlpatterns = [
    path('index/', index, name='index'),
    path('blog/', BlogPage.as_view(), name='blog'),
    path('blog_detail/', blog_detail, name='blog_detail'),
]
