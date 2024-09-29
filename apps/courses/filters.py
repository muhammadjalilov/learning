import django_filters

from apps.courses.models import Course


class CourseFilterBackend(django_filters.FilterSet):
    # category = django_filters.CharFilter(field_name="category", lookup_expr="icontains")
    # price_min = django_filters.NumericRangeFilter(
    #     field_name="published", lookup_expr="gte"
    # )
    # price_max = django_filters.NumericRangeFilter(field_name="price_max", lookup_expr="lte")

    class Meta:
        model = Course
        fields = {'price':['gte', 'lte'],'category':['exact']}
