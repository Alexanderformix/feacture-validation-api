from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import ValidationRule, ValidationTask

from .serializers import ValidationRuleSerializer, ValidationTaskSerializer


class ValidationRuleViewSet(ModelViewSet):

    queryset = ValidationRule.objects.all()
    serializer_class = ValidationRuleSerializer
    permission_classes = [IsAuthenticated]


class ValidationTaskViewSet(ModelViewSet):

    queryset = ValidationTask.objects.all()
    serializer_class = ValidationTaskSerializer
    permission_classes = [IsAuthenticated]
