from django.urls import path

from apps.students.views import StudentCreateAPIView, StudentDetailAPIView

urlpatterns = [
    path('student/', StudentCreateAPIView.as_view(), name='student'),
    path('student/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail')
]
