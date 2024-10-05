from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.quizz.models import Quiz, QuizAttempt
from apps.quizz.serializers import QuizSerializer, QuizAttemptSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class QuizAttemptViewSet(viewsets.ModelViewSet):
    queryset = QuizAttempt.objects.all()
    serializer_class = QuizAttemptSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        attempt = serializer.save()

        return Response({
            'message': 'Quiz completed successfully!',
            'score': attempt.score,
            'completed_at': attempt.completed_at,
        }, status=status.HTTP_201_CREATED)

