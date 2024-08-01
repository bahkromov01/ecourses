from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from .models import Teachers, Comment
from .forms import CommentForm


# Create your views here.


# def teachers(request):
#     return render(request, 'teacher/teacher.html')
# views.py



class TeacherList(View):
    def get(self, request):
        page = request.GET.get('page', '')
        teachers = Teachers.objects.all()
        paginator = Paginator(teachers, 2)
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


class TeacherDetailView(TemplateView):
    template_name = 'teacher/teachers_detail.html'

    def get_context_data(self, **kwargs):
        teacher = Teachers.objects.get(pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['teacher'] = teacher
        return context


def add_comment(request, slug):
    comments = get_object_or_404(Comment, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=True)
            comment.teachers = comment
            comment.save()
            print('Save comment')
            return redirect('teacher_detail')
    else:
        form = CommentForm(request.GET)
        print('get method running')

    return render(request, 'teacher/teachers_detail.html', {'form': form, 'comments': comments})


