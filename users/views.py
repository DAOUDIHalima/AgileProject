# stockManagement/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student,Prof
from .form import ProfForm, StudentForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from datetime import date
from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.templatetags.static import static 

from datetime import timedelta

from django.views.generic import DetailView
import locale
from datetime import date
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, FileResponse

######Prof

def prof_list(request):
    profs = Prof.objects.all()
    return render(request, 'Prof/profs.html', {'profs': profs})

def create_prof(request):
    if request.method == 'POST':
        form = ProfForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        else:
            print("Erreurs du formulaire:", form.errors)  # Affichage des erreurs de formulaire pour débogage
    else:
        form = ProfForm()

    professeurs = Prof.objects.all()
    return render(request, 'Prof/create_prof.html', {'form': form, 'professeurs': professeurs})

def update_prof(request,pk):
    prof=get_object_or_404(Prof,pk=pk)
    if request.method =='POST':
        form=ProfForm(request.POST or None, request.FILES or None ,instance=prof)
        if form.is_valid():
            form.save()
            return redirect('profs')
    else:
        form=ProfForm(instance=Prof)
    return render(request,'Prof/update_prof.html',{'form':form,'prof':prof})

def view_prof(request, pk):
    prof = get_object_or_404(Prof, pk=pk)
    form = ProfForm(instance=prof)
    return render(request, 'Prof/view_prof.html', {'form': form , 'prof':prof})

def delete_prof(pk):
    
    prof = get_object_or_404(Prof,pk=pk)
    prof.delete()
    return redirect('profs')

def home(request):
    return render(request, 'Dashboard/home.html')
def index(request):
    return render(request, 'index.html')

##########Student 

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        else:
            print("Erreurs du formulaire:", form.errors)  # Affichage des erreurs de formulaire pour débogage
    else:
        form = StudentForm()

    students = Student.objects.all()
    return render(request, 'Student/create_student.html', {'form': form, 'students': students})



def student_list(request):
    students = Student.objects.all()
    return render(request, 'Student/students.html', {'students': students})

def view_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=student)
    return render(request, 'student/voir_student.html', {'form': form, 'student': student})

