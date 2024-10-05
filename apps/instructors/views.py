from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.instructors.serializers import InstructorSerializer, InstructorListSerializer
from config.permissions import IsInstructorOrReadOnly
from .models import Instructor
from ..account.permissions import IsOwner
from ..courses.models import Course


class InstructorCreateAPIView(CreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [AllowAny]


class InstructorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class InstructorCoursesListAPIView(ListAPIView):
    serializer_class = InstructorListSerializer
    permission_classes = [IsInstructorOrReadOnly]

    def get_queryset(self):
        return Course.objects.filter(instructor=self.request.user.instructor)
