from django.urls import path
from .views import (
    MascotaListCreateAPIView,
    MascotaDetailAPIView,
    AdopcionCreateAPIView,
    AdopcionDetailAPIView
)

urlpatterns = [
    path('mascotas/', MascotaListCreateAPIView.as_view(), name='mascotas_list_create'),
    path('mascotas/<int:pk>/', MascotaDetailAPIView.as_view(), name='mascota_detail'),
    path('adopciones/', AdopcionCreateAPIView.as_view(), name='adopciones_create'),
    path('adopciones/<int:pk>/', AdopcionDetailAPIView.as_view(), name='adopcion_detail'),
]
