from django.db import models

# Create your models here.


class Fuente(models.Model):
    url = models.URLField
    alias = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.url


class Estimacion(models.Model):
    fuente = models.ForeignKey(Fuente, null=True, on_delete=models.DO_NOTHING)
    fondo = models.TextField(max_length=20)
    valor = models.FloatField
    fecha_hora = models.DateTimeField

    def __str__(self):
        return "{}".format(self.valor)
