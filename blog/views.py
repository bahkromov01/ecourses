from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import get_object_or_404
from django.views import generic, View
from django.views.generic import TemplateView

from courses.forms import CommentForm
from courses.models import Category
from .models import Blog_list, BlogAuthor, BlogComment
from django.contrib.auth.models import User  # Blog author or commenter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse



# def index(request):
#     """
#     View function for home page of site.
#     """
#     # Render the HTML template index.html
#     return render(
#         request,
#         'index.html',
#     )

#
# class BlogListView(generic.ListView):
#
#     model = Blog_list
#     paginate_by = 5
#
#
# class BlogListAuthorView(generic.ListView):
#
#     model = Blog_list
#     paginate_by = 5
#     template_name = 'blog/blog.html'
#
#     def get_queryset(self):
#         id = self.kwargs['pk']
#         target_author = get_object_or_404(BlogAuthor, pk=id)
#         return Blog_list.objects.filter(author=target_author)
#
#     def get_context_data(self, **kwargs):
#         context = super(BlogListAuthorView, self).get_context_data(**kwargs)
#         context['blogger'] = get_object_or_404(BlogAuthor, pk=self.kwargs['pk'])
#         return context
#
#
# class BlogDetailView(generic.DetailView):
#     model = Blog_list
#
#
# class BloggerListView(generic.ListView):
#
#     model = BlogAuthor
#     paginate_by = 5
#
#
# class BlogCommentCreate(LoginRequiredMixin, CreateView):
#     model = BlogComment
#     fields = ['description', ]
#
#     def get_context_data(self, **kwargs):
#         context = super(BlogCommentCreate, self).get_context_data(**kwargs)
#         context['blog'] = get_object_or_404(Blog_list, pk=self.kwargs['pk'])
#         return context
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.instance.blog = get_object_or_404(Blog_list, pk=self.kwargs['pk'])
#         return super(BlogCommentCreate, self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'], })



class BlogListView(View):
    def get(self, request):
        blogs = Blog_list.objects.all()
        categories = Category.objects.all()

        context = {
            'blogs': blogs,
            'categories': categories,
        }
        return render(request, 'blog/blog.html', context)


class BlogDetail(View):
    def get(self, request, slug):
        category = None
        print(slug)
        if slug == '/blog/single/None':
            category = Category.objects.get(slug=slug)
        categories = Category.objects.all()
        num_of_categories = len(categories)

        context = {'category': category,
                   'categories': categories,
                   'num_of_categories': num_of_categories,
                   'active_page': 'blog'}

        return render(request, 'blog/blog_detail.html', context)


class BlogCommentCreate(LoginRequiredMixin, CreateView):

    model = BlogComment
    fields = ['description', ]

    def get_context_data(self, **kwargs):
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog_list, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(Blog_list, pk=self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)