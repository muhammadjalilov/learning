from rest_framework.viewsets import ModelViewSet

from apps.courses.models import Course
from apps.courses.paginations import CustomPagination
from apps.courses.serializers import CoursesSerializer


class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Course.objects.all()
        course_category = self.request.query_params.get('course_category')
        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')
        if course_category:
            queryset = queryset.filter(category=course_category)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        return queryset


