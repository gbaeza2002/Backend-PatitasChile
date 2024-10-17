from django.urls import path
from .views import PrincipalView

urlpatterns = [
    path('api/principal/', PrincipalView.as_view(), name='principal'),
]
