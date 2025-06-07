from django.shortcuts import render
from empleados.models import Empleado

def landing_page(request):
    empleados = Empleado.objects.all()
    return render(request, 'landing/landing.html', {
        'empleados': empleados,
    })
