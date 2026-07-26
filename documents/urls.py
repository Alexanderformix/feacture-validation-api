from rest_framework.routers import DefaultRouter

from .views import DocumentViewSet, DocumentTypeViewSet

router = DefaultRouter()

# Endpoints relacionados con documentos.

router.register("documents", DocumentViewSet)

router.register("document-types", DocumentTypeViewSet)

urlpatterns = router.urls
