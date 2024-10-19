from django.urls import path
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework import permissions


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema

    def get_operation(self, *args, **kwargs):
        operation = super().get_operation(*args, **kwargs)

        lang_header = openapi.Parameter(
            name="Accept-Language",
            description="Description",
            required=False,
            in_=openapi.IN_HEADER,
            type=openapi.IN_QUERY,
            enum=["uz", "ru", "en"],
            default="uz",
        )
        operation.parameters.append(lang_header)
        return operation


schema_view = get_schema_view(
    openapi.Info(
        title="Learning API",
        default_version="v1",
        description="This is a documentation for Learning Backend API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=BothHttpAndHttpsSchemaGenerator,
    urlconf="config.urls",
)

swagger_patterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]