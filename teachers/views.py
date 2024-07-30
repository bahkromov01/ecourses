from django.shortcuts import render, redirect
from django.views import View


# Create your views here.


# def teachers(request):
#     return render(request, 'teacher/teacher.html')
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Teachers, Comment
from .forms import CommentForm


def index(request):
    return render(request, 'app/index.html')


def teacher_list(request):
    teachers = Teachers.objects.all()
    return render(request, 'teacher/teacher.html', {'teachers': teachers})


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teachers, pk=pk)
    comments = teacher.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.teacher = teacher
            comment.save()
            return redirect('teacher_detail', pk=teacher.pk)
    else:
        form = CommentForm()
    return render(request, 'teacher/teachers_detail.html', {'teacher': teacher, 'comments': comments, 'form': form})
