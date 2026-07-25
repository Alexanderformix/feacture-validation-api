from rest_framework import serializers
from .models import ValidationRule, ValidationTask


class ValidationRuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValidationRule
        fields = "__all__"


class ValidationTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValidationTask
        fields = "__all__"
