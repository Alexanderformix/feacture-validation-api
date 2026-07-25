from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"

    ROLES = [
        ("ADMIN", "Administrador"),
        ("USUARIO", "Usuario"),
        ("RRHH", "RRHH"),
        ("CONTABILIDAD", "Contabilidad"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.CharField(max_length=20, choices=ROLES, default="USUARIO")

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Create your models here.
