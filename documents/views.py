from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Document, DocumentType

from .serializers import DocumentSerializer, DocumentTypeSerializer

from validations.models import ValidationRule, ValidationTask
from notifications.models import Notification


class DocumentViewSet(ModelViewSet):

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        document = serializer.save()
        rule = ValidationRule.objects.get(document_type=document.document_type)

        ValidationTask.objects.create(document=document, assigned_to=rule.validator)

        Notification.objects.create(
            user=rule.validator, message=f"Tienes un documento pendiente: {document.id}"
        )


class DocumentTypeViewSet(ModelViewSet):

    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    permission_classes = [IsAuthenticated]
