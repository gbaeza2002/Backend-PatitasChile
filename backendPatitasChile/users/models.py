from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils import timezone
from datetime import timedelta
import random

class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    phone = models.CharField(max_length=15, blank=True, null=True)
    direction = models.CharField(max_length=255, blank=True, null=True)
    
    #Account verification fields
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)
    verification_code_expiration = models.DateTimeField(blank=True, null=True)
    
    #Campos para reestablecimiento de password
    reset_code = models.CharField(max_length=6, blank=True, null=True)
    reset_code_expiration = models.DateTimeField(blank=True, null=True)
    
    #Password reset fields
    def generate_verification_code(self):
        #Generate a 6-digit code and set the expiration time to 10 minutes
        self.verification_code = f"{random.randint(100000, 999999)}"
        self.verification_code_expiration = timezone.now() + timedelta(minutes=10)
        self.save()
        
    def generate_reset_code(self):
        #Generate a password reset code and set the expiration to 10 minutes
        self.reset_code = f"{random.randint(100000, 999999)}"
        self.reset_code_expiration = timezone.now() + timedelta(minutes=10)
        self.save()
        
    def __str__(self):
        return self.username