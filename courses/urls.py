from django.urls import path
from . import views
from .views import CourseDetailView, CourseList, CategoryView
urlpatterns = [
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('courses_list/', CourseList.as_view(), name='courses_list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),

]