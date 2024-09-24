from django.contrib import admin
from .models import Reserva

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'fecha', 'hora', 'numero_personas')

admin.site.register(Reserva, ReservaAdmin)
