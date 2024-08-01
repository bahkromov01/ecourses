from django.urls import path
from . import views
from .views import CourseDetail, CourseList, CategoryView
urlpatterns = [
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('courses_list/', CourseList.as_view(), name='courses_list'),
    path('course_detail/<slug:slug>/', CourseDetail.as_view(), name='course_detail'),

]