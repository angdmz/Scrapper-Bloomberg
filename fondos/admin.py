from django.contrib import admin

# Register your models here.
from fondos.models import Fondo, Cotizacion

admin.site.register(Fondo)
admin.site.register(Cotizacion)
