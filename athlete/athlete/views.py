from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import StudentForm


def home_page(request):
    my_title = "Welcome Athletic Department"
    context = {"title": "my_title"}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
    return render(request,"home.html", context)

def student_page(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,"student.html", {"title": "Welcome Athletes"})

def coach_page(request):
    return render(request, "coach.html", {"title": "Welcome Coaches"})

def example_page(request):
    context = {"title": "Example"}
    template_name = "hello.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))
    # (request, "coach.html", {"title": "Welcome Coaches"})