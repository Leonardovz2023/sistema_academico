# registro/models.py

from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        abstract = True

class Alumno(Persona):
    matricula = models.CharField(max_length=10)
    carrera = models.CharField(max_length=100)

class Profesor(Persona):
    cedula = models.CharField(max_length=10)
    especialidad = models.CharField(max_length=100)
