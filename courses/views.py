from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from teachers.models import Teachers
from .forms import CourseForm, CommentForm
from .models import Course, Category

class IndexPage(View):
    def get(self, request):
        categories = Category.objects.all()
        teachers = (Teachers.objects.all())
        courses = Course.objects.all()

        context = {'categories': categories,
                   'teachers': teachers,
                   'courses': courses,
                   'active_page': 'home'}

        return render(request, 'app/index.html', context)

# def category(request, pk):
#     categories = Category.objects.all()
#     return render(request, 'course/course.html', {'categories': categories})


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'course/course.html', {'categories': categories})


# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'course/course.html', {'courses': courses})

class CourseList(View):
    def get(self, request):
        page = request.GET.get('page', '')
        courses = Course.objects.all()
        paginator = Paginator(courses, 1)
        categories = Category.objects.all()

        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(Paginator.num_pages)

        context = {
            'page_obj': page_obj,
            'categories': categories
        }
        return render(request, 'course/course.html', context)


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

