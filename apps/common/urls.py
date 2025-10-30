from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.api_endpoints.answers.views import StudentAnswerViewSet

router = DefaultRouter()
router.register('answers', StudentAnswerViewSet, basename='answer')

urlpatterns = router.urls

