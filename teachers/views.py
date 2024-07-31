from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.


# def teachers(request):
#     return render(request, 'teacher/teacher.html')
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Teachers
from .forms import CommentForm



class TeacherList(View):
    def get(self, request):
        page = request.GET.get('page', '')
        teachers = Teachers.objects.all()
        paginator = Paginator(teachers, 1)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(Paginator.num_pages)

        context = {
            'page_obj': page_obj,
        }
        return render(request, 'teacher/teacher.html', context)


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
