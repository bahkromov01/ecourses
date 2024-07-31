from django.urls import path

from . import views
from .views import TeacherList, teacher_detail

urlpatterns = [
    path('teachers/',TeacherList.as_view(), name='teachers'),
    path('teacher_detail/<int:pk>/', teacher_detail, name='teacher_detail'),
    # Add other URL patterns here
]