from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    message = models.TextField()

    read = models.BooleanField(
        default=False
    )

# Create your models here.
