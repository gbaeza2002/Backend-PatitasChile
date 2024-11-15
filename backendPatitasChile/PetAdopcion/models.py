from django.db import models
from users.models import User
from django.utils import timezone

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)  
    raza = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    edad= models.CharField(max_length=2)
    direccion = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mascotas')  
    is_adopted = models.BooleanField(default=False)  

    def __str__(self):
        return self.nombre


class Adopcion(models.Model):
    userRut = models.CharField(max_length=12)
    mascotaId = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='adopciones')
    fechaAdopcion = models.DateTimeField(default=timezone.now)  # Fecha se registra automáticamente
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adopciones')

    def __str__(self):
        return f"Adopción de {self.mascotaId.nombre} por {self.usuario.email}"