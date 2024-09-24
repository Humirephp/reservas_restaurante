from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_reservas, name='lista_reservas'),
    path('nueva/', views.crear_reserva, name='crear_reserva'),
    path('editar/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),
    path('eliminar/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),  # Nueva línea
]

