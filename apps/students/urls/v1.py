from django.urls import path

from apps.students.views import StudentCreateAPIView, StudentDetailAPIView, StudentCoursesList, StudentCourseRetrieve

urlpatterns = [
    path('student/', StudentCreateAPIView.as_view(), name='student'),
    path('student-courses/', StudentCoursesList.as_view(), name='student_courses'),
    path('student/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('student-courses/<int:pk>/', StudentCourseRetrieve.as_view(), name='student-course-detail'),
]
