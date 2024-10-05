from django.template.context_processors import request
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from apps.courses.filters import CourseFilterBackend
from apps.courses.models import Course, Category, Chapter, Topic
from apps.courses.paginations import CustomPagination
from apps.courses.serializers import CoursesSerializer, CategorySerializer, ChapterSerializer, TopicSerializer


class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CourseFilterBackend

    def get_queryset(self):
        return self.queryset.filter(instructor=self.request.user.instructor)


    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user.instructor)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ChapterViewSet(ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


