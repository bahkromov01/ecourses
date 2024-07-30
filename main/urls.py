from django.urls import path

from main.views import index, about, contact, login

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contact/',contact, name='contact'),
    path('login/', login, name='login'),
]