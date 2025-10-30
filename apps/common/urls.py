from django.urls import include, path
from apps.assignments.api_endpoints.answers.views import StudentAnswerViewSet



urlpatterns = [
    path('answers/', StudentAnswerViewSet.as_view({'get': 'list'}), name='answer-list'),
    path('answers/<int:pk>/', StudentAnswerViewSet.as_view({'get': 'retrieve'}), name='answer-detail'),
    path('answers-list/', StudentAnswerViewSet.as_view({'get': 'list'}), name='answer_list'),
]

