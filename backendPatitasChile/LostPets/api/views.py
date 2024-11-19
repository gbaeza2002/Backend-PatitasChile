from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from LostPets.models import LostPet
from LostPets.api.serializer import LostPetSerializer
from django.shortcuts import get_object_or_404

# Vista para listar y crear reportes de mascotas perdidas
class LostPetListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        lost_pets = LostPet.objects.all()
        serializer = LostPetSerializer(lost_pets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LostPetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)  # Asigna automáticamente el usuario autenticado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para obtener, actualizar y eliminar un reporte específico de mascota perdida
class LostPetDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        lost_pet = get_object_or_404(LostPet, pk=pk)
        serializer = LostPetSerializer(lost_pet)
        return Response(serializer.data)

    def put(self, request, pk):
        lost_pet = get_object_or_404(LostPet, pk=pk)
        serializer = LostPetSerializer(lost_pet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        lost_pet = get_object_or_404(LostPet, pk=pk)
        lost_pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
