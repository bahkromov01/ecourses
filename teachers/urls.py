from django.urls import path

from . import views
from .views import TeacherList, TeacherDetailView, add_comment

urlpatterns = [
    path('teachers/',TeacherList.as_view(), name='teachers'),
    path('teachers/<int:pk>', TeacherDetailView.as_view(), name='teacher_detail'),
    path('add_comment/<slug:slug>', add_comment, name='add_comment'),
    # Add other URL patterns here
]