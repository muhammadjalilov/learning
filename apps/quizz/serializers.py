from rest_framework import serializers

from apps.quizz.models import Quiz, Question, Choice


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        exclude = 'created_at', 'updated_at'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = 'created_at', 'updated_at'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        exclude = 'created_at', 'updated_at'
