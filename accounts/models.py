from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.managers import CustomManager

# Create your models here.
class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = "admin"
        USER = "user"
    
    role = models.CharField(max_length=5, choices=RoleChoices.choices, default=RoleChoices.USER)

    objects = CustomManager()

    def is_admin(self):
        return self.role == self.RoleChoices.ADMIN