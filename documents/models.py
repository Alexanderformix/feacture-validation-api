from django.db import models
from django.contrib.auth.models import User


class DocumentType(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Document(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected')
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.CASCADE
    )

    file = models.FileField(
        upload_to='documents/'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
# Create your models here.
