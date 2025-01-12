from rest_framework import serializers
from LostPets.models import LostPet

class LostPetSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)  # Solo lectura para asignar automáticamente

    class Meta:
        model = LostPet
        fields = [
            'id', 'name', 'species', 'breed', 'last_seen_location',
            'last_seen_date', 'contact_info', 'additional_details', 'photo', 'owner'
        ]

