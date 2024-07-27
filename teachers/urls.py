from django.urls import path

from main.views import index
from . import views
from .views import teachers

urlpatterns = [
    path('index/', index, name='index'),
    path('teachers/', teachers, name='teachers')
    # Add other URL patterns here
]