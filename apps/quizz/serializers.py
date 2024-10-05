from rest_framework import serializers

from apps.instructors.serializers import InstructorSerializer
from apps.quizz.models import Quiz, Question, Answer, UserAnswer, QuizAttempt


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'choice', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question', 'answers']


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    num_questions = serializers.ReadOnlyField()
    creator = InstructorSerializer(read_only=True)


    class Meta:
        model = Quiz
        fields = ['id', 'name', 'description', 'questions', 'created_at', 'num_questions', 'creator']


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['question', 'selected_answer']


class QuizAttemptSerializer(serializers.ModelSerializer):
    user_answers = UserAnswerSerializer(many=True)

    class Meta:
        model = QuizAttempt
        fields = ['quiz', 'user_answers', 'score', 'completed_at']

    def create(self, validated_data):
        user = self.context['request'].user
        quiz = validated_data['quiz']
        user_answers_data = validated_data.pop('user_answers')

        attempt = QuizAttempt.objects.create(user=user, quiz=quiz, score=0.0)

        total_questions = quiz.questions.count()
        correct_answers = 0

        for user_answer_data in user_answers_data:
            question = user_answer_data['question']
            selected_answer = user_answer_data['selected_answer']

            UserAnswer.objects.create(attempt=attempt, question=question, selected_answer=selected_answer)

            if selected_answer.is_correct:
                correct_answers += 1

        attempt.score = (correct_answers / total_questions) * 100
        attempt.save()

        return attempt
