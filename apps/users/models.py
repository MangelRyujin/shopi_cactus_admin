from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    email = models.EmailField('Correo Electrónico', max_length=255 , unique=True, blank = False, null= False)
    
    class Meta:    
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name']
    
    def natural_key(self):
        return (self.username)
    
    def __str__(self) -> str:
        return self.username