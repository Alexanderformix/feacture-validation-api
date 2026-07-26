from django.db import models
from django.contrib.auth.models import User

# Representa los tipos de documentos permitidos.


class DocumentType(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documento"

    def __str__(self):
        return self.name


# Documento cargado por un usuario.


class Document(models.Model):

    ESTADOS = [
        ("PENDIENTE", "Pendiente"),
        ("APROBADO", "Aprobado"),
        ("RECHAZADO", "Rechazado"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)

    file = models.FileField(upload_to="documents/")

    status = models.CharField(max_length=20, choices=ESTADOS, default="PENDIENTE")

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
