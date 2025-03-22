from django.db import models

# Create your models here.
class Alumno(models.Model):
    numControl = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    primerAp = models.CharField(max_length=100)
    segundoAp = models.CharField(max_length=100)
    fecha_Nac = models.DateField()
    semestre = models.IntegerField()
    carrera = models.CharField(max_length=100)

class Meta:
    db_table = 'Alumnos'

