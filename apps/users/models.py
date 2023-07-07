from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
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
    
    def save(self, *args,**kargs):
        if not User.objects.filter(pk = self.pk).exists() and User.objects.exists():
            raise ValidationError("There can by only User admin register")
        return super(User,self).save(*args,**kargs)