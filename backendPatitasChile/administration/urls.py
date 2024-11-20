from django.urls import path
from .views import dashboard_view
from django.shortcuts import render

def no_autorizado_view(request):
    return render(request, 'dashboard/noAutorizado.html', status=403)


urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('no-autorizado/', no_autorizado_view, name='no-autorizado'),
]

