from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from blog.models import Blog_list
from teachers.models import Teachers
from .forms import CourseForm, CommentForm
from .models import Course, Category, Comment


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


class CourseDetailView(TemplateView):
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        blogs = Blog_list.objects.all()
        categories = Category.objects.all()
        blog = Blog_list.objects.get(pk=self.kwargs['pk'])
        comments = blog.comments.all()
        authors = blog.auther_id.all()
        context = super().get_context_data(**kwargs)
        context['blog'] = blog
        context['authors'] = authors
        context['categories'] = categories
        context['blogs'] = blogs
        context['comments'] = comments
        return context

    def post(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog_list, pk=self.kwargs['pk'])
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.is_published = True
            comment.blog_id = blog
            comment.save()
            return redirect(reverse('blog-detail', kwargs={'pk': blog.pk}))
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


