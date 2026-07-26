from django.db import models
from django.contrib.auth.models import User

# Notificaciones internas generadas por el sistema.


class Notification(models.Model):

    class Meta:
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    message = models.TextField()

    read = models.BooleanField(default=False)
