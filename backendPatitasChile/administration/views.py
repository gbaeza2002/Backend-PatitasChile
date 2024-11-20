from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
import json
from django.db.models.functions import TruncMonth
from PetAdopcion.models import Mascota
from users.models import User
from django.db import models
from datetime import datetime

# Decorador para verificar si el usuario es administrador
def is_admin(user):
    return user.is_superuser  # Verifica si el usuario es un superusuario (admin)

@user_passes_test(is_admin, login_url='no-autorizado/')

def dashboard_view(request):
    # Datos existentes
    total_lost_pets = Mascota.objects.filter(descripcion__icontains='perdida').count()
    total_adoptable_pets = Mascota.objects.filter(is_adopted=False).count()
    total_users = User.objects.count()

    # Cantidad de mascotas por especie
    species_count = Mascota.objects.values('especie').annotate(count=models.Count('id'))
    species_data = json.dumps(list(species_count))  # Convertimos los datos a JSON

    # Proporción adoptadas/no adoptadas
    adoption_stats = {
        "adoptadas": Mascota.objects.filter(is_adopted=True).count(),
        "no_adoptadas": Mascota.objects.filter(is_adopted=False).count(),
    }
    adoption_data = json.dumps(adoption_stats)

    # Crecimiento de usuarios por mes
    users_by_month = User.objects.annotate(month=TruncMonth('date_joined')).values('month').annotate(count=models.Count('id')).order_by('month')
    
    # Convertir el campo 'month' a string antes de serializarlo
    user_growth_data = json.dumps([{
        'month': user['month'].strftime('%Y-%m'),  # Formatear la fecha
        'count': user['count']
    } for user in users_by_month])

    # Información del usuario actual
    user_email = request.user.email  # Correo del usuario
    user_joined_date = request.user.date_joined  # Fecha de registro del usuario
    # Calcular antigüedad en años
    current_date = datetime.now()
    user_seniority = current_date.year - user_joined_date.year - ((current_date.month, current_date.day) < (user_joined_date.month, user_joined_date.day))

    # Obtener los últimos usuarios registrados
    recent_users = User.objects.all().order_by('-date_joined')[:5]  # Últimos 5 usuarios registrados

    context = {
        'total_lost_pets': total_lost_pets,
        'total_adoptable_pets': total_adoptable_pets,
        'total_users': total_users,
        'species_data': species_data,
        'adoption_data': adoption_data,
        'user_growth_data': user_growth_data,
        'user_email': user_email,  # Correo del usuario
        'user_seniority': user_seniority,  # Antigüedad del usuario
        'recent_users': recent_users,  # Últimos usuarios registrados
    }
    return render(request, 'dashboard/dashboard.html', context)

# Vista para manejar redirección en caso de no estar autorizado
def no_autorizado_view(request):
    return render(request, 'dashboard/no_autorizado.html', status=403)
