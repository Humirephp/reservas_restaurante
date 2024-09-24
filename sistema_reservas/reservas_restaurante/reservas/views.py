
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm

def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})

def crear_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/crear_reserva.html', {'form': form})

def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)  # Obtiene la reserva por ID
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)  # Vuelve a crear el formulario con los datos de la reserva
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('lista_reservas')  # Redirige a la lista de reservas
    else:
        form = ReservaForm(instance=reserva)  # Si no es POST, muestra el formulario con los datos existentes
    return render(request, 'reservas/editar_reserva.html', {'form': form})  # Renderiza el template

def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)  # Obtiene la reserva
    reserva.delete()  # Elimina la reserva
    return redirect('lista_reservas')  # Redirige a la lista de reservas
