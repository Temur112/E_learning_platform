from django.urls import path
from . import views


app_name = 'students'
urlpatterns = [
    path('register/', views.StudentRegistrationForm.as_view(), name='student_registration'),
    path('enroll-course/', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path(
        'courses/',
        views.StudentCourseListView.as_view(),
        name='student_course_list'
    ),
    path(
        'course/<int:pk>/',
        views.StudentCourseDetailView.as_view(),
        name='student_course_detail'
    ),
    path(
        'course/<pk>/<modules_id>/',
        views.StudentCourseDetailView.as_view(),
        name='student_course_detail_module'
    ),
]
