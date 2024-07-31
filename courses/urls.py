from django.urls import path
from . import views
from .views import courses_detail, CourseList, CategoryView
urlpatterns = [
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('courses_list/', CourseList.as_view(), name='courses_list'),
    path('course_detail/<int:pk>/', courses_detail, name='course_detail'),

]