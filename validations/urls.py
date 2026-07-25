from rest_framework.routers import DefaultRouter

from .views import ValidationRuleViewSet, ValidationTaskViewSet

router = DefaultRouter()

router.register("validation-rules", ValidationRuleViewSet)

router.register("validation-tasks", ValidationTaskViewSet)

urlpatterns = router.urls
