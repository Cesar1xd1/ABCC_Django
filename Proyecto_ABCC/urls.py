"""
URL configuration for Proyecto_ABCC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from servicios_escolares.views import ListaAlumnos,DetalleAlumno,CrearAlumno,ModificarAlumno,EliminarAlumno,login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumnos/',ListaAlumnos.as_view(template_name="alumnos/index.html"),name="listar"),
    path('alumnos/detalle/<int:pk>',DetalleAlumno.as_view(template_name="alumnos/detalle.html"),name="detalle"),
    path('alumnos/crear',CrearAlumno.as_view(template_name="alumnos/crear.html"),name="crear"),
    path('alumnos/editar/<int:pk>',ModificarAlumno.as_view(template_name="alumnos/editar.html"),name="editar"),
    path('eliminar/<int:pk>/', EliminarAlumno.as_view(), name='eliminar'),
    path('', login, name='login'),
   
    

]
