from rest_framework import serializers
from ..models import Mascota, Adopcion
from users.models import User  # Asegúrate de importar User si lo necesitas en algún serializer

class MascotaSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(read_only=True)  # Solo lectura para asignar automáticamente

    class Meta:
        model = Mascota
        fields = ['id', 'nombre', 'genero', 'especie', 'raza', 'usuario', 'is_adopted']

class AdopcionSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(read_only=True)
    mascotaId = serializers.PrimaryKeyRelatedField(queryset=Mascota.objects.all())

    class Meta:
        model = Adopcion
        fields = ['id', 'userRut', 'mascotaId', 'usuario']
