import django_filters

from apps.courses.models import Course


class CourseFilterBackend(django_filters.FilterSet):

    class Meta:
        model = Course
        fields = {'price':['gte', 'lte'],'category':['exact']}
