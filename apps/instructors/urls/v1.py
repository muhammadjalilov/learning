from collections import namedtuple

from django.urls import path

from apps.instructors.views import InstructorCreateAPIView, InstructorDetailAPIView

app_name = 'instructors'
urlpatterns = [
    path('instructors', InstructorCreateAPIView.as_view(), name='instructors'),
    path('instructors/<int:pk>/', InstructorDetailAPIView.as_view(), name='instructors-detail'),
]
