from .models import Course, Comment
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'number_of_students', 'price', 'duration', 'video', 'category']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment', 'rating']


