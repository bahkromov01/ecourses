
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm, CommentForm
from .models import Course, Category, Comment


def index(request):
    return render(request, 'app/index.html')


def category(request, pk):
    categories = Category.objects.all()
    return render(request, 'course/course.html', {'categories': categories})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course.html', {'courses': courses})


def courses_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.course = course
            comment.save()
            return redirect('course_detail', pk=course.pk)
    else:
        comment_form = CommentForm()
    comments = course.comments.all()
    return render(request, 'course/course_detail.html', {
        'course': course,
        'comment_form': comment_form,
        'comments': comments
    })



