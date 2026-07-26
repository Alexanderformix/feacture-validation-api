from django.test import TestCase
from django.contrib.auth.models import User
from documents.models import DocumentType


class DocumentTypeTest(TestCase):

    def test_create_document_type(self):

        doc = DocumentType.objects.create(name="Factura")

        self.assertEqual(doc.name, "Factura")
