from django.db import models

class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    numero_personas = models.IntegerField()

    def __str__(self):
        return f"Reserva de {self.nombre_cliente} para {self.numero_personas} personas."
