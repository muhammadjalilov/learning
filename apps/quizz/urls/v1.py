from django.urls import include, path
from rest_framework import routers

from apps.quizz.views import QuizViewSet, QuizAttemptViewSet

router = routers.DefaultRouter()
router.register('quizzes', QuizViewSet, basename='quizzes')
router.register('questions', QuizAttemptViewSet, basename='quizattempt')

app_name = 'quizz'

urlpatterns = [
    path('', include(router.urls)),
]