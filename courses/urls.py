from django.urls import path

from main.views import index
from . import views
from .views import courses

urlpatterns = [
    path('index/', index, name='index'),
    path('courses/', courses, name='courses')
]