from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size = 30
    page_size_query_param = "size"
