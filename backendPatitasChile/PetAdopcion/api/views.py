from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from PetAdopcion.models import Mascota, Adopcion
from PetAdopcion.api.serializer import MascotaSerializer, AdopcionSerializer
from django.shortcuts import get_object_or_404

# Vista para listar y crear mascotas (requiere autenticación)
class MascotaListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario=request.user)  # Asigna automáticamente el usuario autenticado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para obtener, actualizar y eliminar una mascota específica (requiere autenticación)
class MascotaDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        mascota = get_object_or_404(Mascota, pk=pk)
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)

    def put(self, request, pk):
        mascota = get_object_or_404(Mascota, pk=pk)
        serializer = MascotaSerializer(mascota, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mascota = get_object_or_404(Mascota, pk=pk)
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vista para registrar una adopción (requiere autenticación)
class AdopcionCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        mascota = get_object_or_404(Mascota, id=request.data.get('mascotaId'))
        if mascota.is_adopted:
            return Response({"detail": "Esta mascota ya ha sido adoptada."}, status=status.HTTP_400_BAD_REQUEST)
        mascota.is_adopted = True
        mascota.save()
        serializer = AdopcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario=request.user, mascotaId=mascota)  # Asigna el usuario autenticado y la mascota
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para obtener, actualizar y eliminar una adopción específica (requiere autenticación)
class AdopcionDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        adopcion = get_object_or_404(Adopcion, pk=pk)
        serializer = AdopcionSerializer(adopcion)
        return Response(serializer.data)

    def put(self, request, pk):
        adopcion = get_object_or_404(Adopcion, pk=pk)
        serializer = AdopcionSerializer(adopcion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        adopcion = get_object_or_404(Adopcion, pk=pk)
        adopcion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

