from django.db import models

class Colegios(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    mail = models.EmailField(max_length=100)

    def _str_(self):
        return self.nombre
    
class Alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    promedio = models.DecimalField(max_digits=4, decimal_places=2)

    def _str_(self):
        return self.nombre
    
class Asignaturas(models.Model):
    nombre = models.CharField(max_length=100)
    cargaHoraria = models.IntegerField()
    examenes = models.IntegerField()

    def _str_(self):
        return self.nombre