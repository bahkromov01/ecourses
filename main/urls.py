from django.urls import path

from blog.views import blog
from main.views import index, about, contact

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contact/',contact, name='contact'),
]