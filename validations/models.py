from django.db import models
from django.contrib.auth.models import User

from documents.models import (
    Document,
    DocumentType
)


class ValidationRule(models.Model):
    class Meta:
        verbose_name = "Regla de Validación"
        verbose_name_plural = "Reglas de Validación"

    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.CASCADE
    )

    validator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class ValidationTask(models.Model):
    class Meta:
        verbose_name = "Tarea de Validación"
        verbose_name_plural = "Tareas de Validación"

    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    completed = models.BooleanField(
        default=False
    )

# Create your models here.
