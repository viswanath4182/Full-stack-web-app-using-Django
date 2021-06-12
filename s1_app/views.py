from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, RegData
from .forms import RegForm


def home(request):
    objs = Student.objects.all()
    context = {'home': 'This is the home page of a student',
               'objs': objs}

    return render(request, 'home.html', context)

def marks(request):
    marks = {'marks': [10, 20, 62, 30, 51],
             'is_goodstudent': True}
    return render(request, 'marks.html', marks)

def ranks(request):
    context = {'list': [1, 2, 5, 8, 9, 1]
               }
    return render(request, 'ranks.html', context)
def name_year(request, year):
    objects = Student.objects.filter(birth_year=year)
    context = {'objects': objects,
               'year': year}
    return render(request, 'year_filter.html', context)

def register(request):
    form = RegForm()
    context = {'form': form}
    return render(request, 'home.html', context)
def addUser(request):
    form = RegForm(request.POST)
    if form.is_valid():
        registered_data=RegData(username=form.cleaned_data['username'], name=form.cleaned_data['name'],
                                password=form.cleaned_data['password'], number=form.cleaned_data['number'])
        registered_data.save()
    return redirect('home')







