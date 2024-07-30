from django.urls import path

from main.views import index
from . import views
from .views import courses_detail, course_list, category

urlpatterns = [
    path('index/', index, name='index'),
    path('category/<int:pk>/', category, name='category'),
    path('courses_list/', course_list, name='courses_list'),
    path('course_detail/<int:pk>/', courses_detail, name='course_detail'),
]