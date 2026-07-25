from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/documents/", include("documents.urls")),
    path("api/validations/", include("validations.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
]
