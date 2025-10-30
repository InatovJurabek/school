from django.urls import path
from apps.assignments import views
from apps.api_endpoints.answers.views import StudentAnswerViewSet

urlpatterns = [
    path('answers/', StudentAnswerViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-answer-list'),
    path("answers/", views.index, name="answers-list"),
    path("answers/<int:pk>/", views.detail, name="answers-detail"),
]

