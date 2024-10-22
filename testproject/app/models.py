from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=512)

    def __str__(self):
        return str(self.titulo)
 
class Puesto(models.Model):
    status = models.BooleanField(default=True)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pelicula)+" | "+str(self.status)