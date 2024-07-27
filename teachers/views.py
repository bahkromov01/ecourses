from django.shortcuts import render

# Create your views here.


def teachers(request):
    return render(request,'teacher/teacher.html')
