from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Document, DocumentType

from .serializers import DocumentSerializer, DocumentTypeSerializer


class DocumentViewSet(ModelViewSet):

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]


class DocumentTypeViewSet(ModelViewSet):

    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    permission_classes = [IsAuthenticated]
