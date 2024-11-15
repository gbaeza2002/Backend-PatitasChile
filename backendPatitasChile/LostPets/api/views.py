from rest_framework import viewsets
from LostPets.models import LostPet
from LostPets.api.serializer import LostPetSerializer
from rest_framework.permissions import IsAuthenticated

class LostPetViewSet(viewsets.ModelViewSet):
    queryset = LostPet.objects.all()
    serializer_class = LostPetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Asigna el usuario autenticado como el propietario (owner)
