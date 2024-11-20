from django.db import models
from users.models import User  

class LostPet(models.Model):
    PET_SPECIES = [
        ('Dog', 'Perro'),
        ('Cat', 'Gato'),
        ('Other', 'Otro'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lost_pets", verbose_name="Usuario")
    name = models.CharField(max_length=100, verbose_name="Nombre Mascota")
    species = models.CharField(max_length=50, choices=PET_SPECIES, verbose_name="Especie")
    breed = models.CharField(max_length=100, verbose_name="Raza", blank=True, null=True)
    last_seen_location = models.CharField(max_length=255, verbose_name="Última vez visto")
    last_seen_date = models.DateField(verbose_name="Último día visto")#YYYY-MM-DD. MODIFICAR
    contact_info = models.CharField(max_length=100, verbose_name="Información de contacto")
    additional_details = models.TextField(verbose_name="Detalles adicionales", blank=True, null=True)
    photo = models.ImageField(upload_to='pet_photos/', verbose_name="Foto de la mascota", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.species}"

    class Meta:
        verbose_name = "Mascota perdida"
        verbose_name_plural = "Mascotas perdidas"
