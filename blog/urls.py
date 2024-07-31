from django.urls import path
from . import views
from .views import BlogDetail, BlogPage, CommentPage, AuthorPage
urlpatterns = [
    path('blog/', BlogPage.as_view(), name='blog'),
    path('blog_detail/', BlogDetail.as_view(), name='blog_detail'),
    path('comments/', CommentPage.as_view(), name='comments'),
    path('authors/', AuthorPage.as_view(), name='authors'),

]
