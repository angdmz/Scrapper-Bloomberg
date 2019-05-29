from django.db import models

# Create your models here.


class Fondo(models.Model):
    nombre = models.CharField(max_length=30)
    codigo = models.CharField(max_length=20, null=True)
    descripcion = models.TextField(max_length=120)
    fecha_apertura_fondo = models.DateField
    hora_inicio_actividad = models.TimeField
    hora_fin_actividad = models.TimeField

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        db_table = 'fondo'
        verbose_name = 'Fondo de inversion'
        verbose_name_plural = 'Fondos de inversion'


class Cotizacion(models.Model):
    costo_cuotaparte = models.FloatField
    fondo = models.ForeignKey(Fondo, db_column='fondo_id', on_delete=models.CASCADE)
    dia = models.DateField

    def __str__(self):
        return "{} {}".format(self.fondo, self.costo_cuotaparte)

    class Meta:
        db_table = 'cotizacion'
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'
