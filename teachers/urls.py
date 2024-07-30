from django.urls import path

from main.views import index
from . import views
from .views import teacher_list, teacher_detail

urlpatterns = [
    path('index/', index, name='index'),
    path('teachers/', teacher_list, name='teachers'),
    path('teacher_detail/<int:pk>/', teacher_detail, name='teacher_detail'),
    # Add other URL patterns here
]