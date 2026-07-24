from django.db import models
from django.contrib.auth.models import User

from documents.models import (
    Document,
    DocumentType
)


class ValidationRule(models.Model):

    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.CASCADE
    )

    validator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class ValidationTask(models.Model):

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
