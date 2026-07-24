from django.contrib import admin
from .models import ValidationRule, ValidationTask

admin.site.register(ValidationRule)
admin.site.register(ValidationTask)

# Register your models here.
