from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from .models import Alumno

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.urls import reverse_lazy

class ListaAlumnos(ListView):
    model = Alumno

#---Altas---
class CrearAlumno(SuccessMessageMixin,CreateView):
    model = Alumno
    fields = "__all__"
    success_message = "Alumno AGREGADO Correctamente"
    success_url = "/alumnos"  
#---Bajas---

def login(request):
    return render(request, 'alumnos/login.html')

class EliminarAlumno(DeleteView):
    model = Alumno
    success_url = reverse_lazy('listar') 
#---Cambios---
class ModificarAlumno(SuccessMessageMixin,UpdateView):
    model = Alumno
    form = Alumno
    fields = "__all__"
    success_message = "Alumno MODIFICADO Correctamente"
    def get_success_url(self):
        return reverse('listar')



#---Consultas---
class DetalleAlumno(DetailView):
    model = Alumno