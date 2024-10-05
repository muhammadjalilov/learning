from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.account.permissions import IsOwner
from apps.courses.models import Course
from apps.courses.serializers import CoursesSerializer
from apps.students.models import Student
from apps.students.serializers import StudentSerializer
from config.permissions import IsStudentOrReadOnly


class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]


class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class StudentCoursesList(generics.ListAPIView):
    serializer_class = CoursesSerializer
    permission_classes = [IsStudentOrReadOnly]

    def get_queryset(self):
        queryset = Course.objects.filter(students=self.request.user.student)
        return queryset

class StudentCourseRetrieve(generics.RetrieveAPIView):
    serializer_class = CoursesSerializer
    permission_classes = [IsStudentOrReadOnly]

    def get_queryset(self):
        queryset = Course.objects.filter(students=self.request.user.student)
        return queryset
