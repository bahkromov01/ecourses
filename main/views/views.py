
from django.shortcuts import render, redirect
from django.views import View

from confic import settings
from courses.models import Category
from main.forms import ContactForm, EmailForm
from main.models import Contact
from teachers.models import Teachers
from courses.models import Course


# Create your views here.


class IndexPage(View):
    def get(self, request):
        categories = Category.objects.all()
        teachers = Teachers.objects.all()
        courses = Course.objects.all()

        context = {'categories': categories,
                   'teachers': teachers,
                   'courses': courses,
                   'active_page': 'home'}

        return render(request, 'app/index.html', context)


def about(request):
    return render(request, 'app/about.html')


def contact(request):
    contacts = Contact.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'app/contact.html', {'form': form, 'contacts': contacts})





