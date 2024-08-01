from django.urls import path
from . import views
from .views import BlogDetailView, BlogCommentCreate, BlogListView
urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/comment/', BlogCommentCreate.as_view(), name='blog_comment'),

]
