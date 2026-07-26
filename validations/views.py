from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import ValidationRule, ValidationTask

from .serializers import ValidationRuleSerializer, ValidationTaskSerializer

from documents.models import Document
from notifications.models import Notification

from rest_framework.decorators import action
from rest_framework.response import Response


class ValidationRuleViewSet(ModelViewSet):

    queryset = ValidationRule.objects.all()
    serializer_class = ValidationRuleSerializer
    permission_classes = [IsAuthenticated]


class ValidationTaskViewSet(ModelViewSet):

    queryset = ValidationTask.objects.all()
    serializer_class = ValidationTaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ValidationTask.objects.filter(assigned_to=self.request.user)

    @action(detail=True, methods=["post"])
    def approve(self, request, pk=None):

        task = self.get_object()

        if task.assigned_to != request.user:
            return Response({"error": "No tienes permisos."}, status=403)

        if task.completed:
            return Response({"error": "Esta tarea ya fue procesada."}, status=400)

        task.document.status = "APROBADO"
        task.document.save()

        task.completed = True
        task.save()

        Notification.objects.create(
            user=task.document.user, message="Tu documento fue aprobado."
        )

        return Response({"message": "Documento aprobado."})

    """
    Permite al usuario responsable aprobar un documento.
    Solo el usuario asignado puede ejecutar esta acción.
    """

    @action(detail=True, methods=["post"])
    def reject(self, request, pk=None):

        task = self.get_object()

        if task.assigned_to != request.user:
            return Response({"error": "No tienes permisos."}, status=403)

        if task.completed:
            return Response({"error": "Esta tarea ya fue procesada."}, status=400)

        task.document.status = "RECHAZADO"
        task.document.save()

        task.completed = True
        task.save()

        Notification.objects.create(
            user=task.document.user, message="Tu documento fue rechazado."
        )

        return Response({"message": "Documento rechazado."})

    """
    Permite al usuario responsable aprobar un documento.
    Solo el usuario asignado puede ejecutar esta acción.
    """
