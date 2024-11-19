from django.urls import path
from .views import LostPetListCreateAPIView, LostPetDetailAPIView

urlpatterns = [
    path('lost-pets/', LostPetListCreateAPIView.as_view(), name='lost_pets_list_create'),
    path('lost-pets/<int:pk>/', LostPetDetailAPIView.as_view(), name='lost_pet_detail'),
]
