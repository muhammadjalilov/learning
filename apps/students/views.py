from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.account.permissions import IsOwner
from apps.courses.models import Course
from apps.students.models import Student
from apps.students.serializers import StudentSerializer


class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsOwner]
