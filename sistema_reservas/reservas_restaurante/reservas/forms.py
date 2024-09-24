from django import forms
from .models import Reserva
from datetime import date, time  # Importa date y time

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_cliente', 'fecha', 'hora', 'numero_personas']

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha < date.today():
            raise forms.ValidationError("La fecha no puede ser anterior a hoy.")
        return fecha

    def clean_hora(self):
        hora = self.cleaned_data.get('hora')
        if hora < time(10, 0) or hora > time(22, 0):  # Verifica la hora
            raise forms.ValidationError("La hora debe estar entre las 10:00 y las 22:00.")
        return hora
