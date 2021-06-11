from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def home(request):
    obj = Student.objects.get(id=1)
    context = {'home': 'This is the home page of a student',
               'obj': obj}

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





