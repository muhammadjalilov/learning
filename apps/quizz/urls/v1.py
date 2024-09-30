from django.urls import include, path
from rest_framework import routers

from apps.courses.views import CategoryViewSet
from apps.quizz.views import QuizViewSet, QuestionViewSet, ChoiceViewSet

router = routers.DefaultRouter()
router.register('quizzes', QuizViewSet, basename='quizzes')
router.register('questions', QuestionViewSet, basename='questions')
router.register('choices', ChoiceViewSet, basename='choices')

app_name = 'quizz'

urlpatterns = [
    path('', include(router.urls)),
]