from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

app_name = 'api_courses'

router.register('courses', views.CourseViewSet)
router.register('subjects', views.SubjectViewSet)
urlpatterns = [
    # path(
    #     'subjects/',
    #     views.SubjectListView.as_view(),
    #     name='subject_list',
    # ),
    # path(
    #     'subjects/<int:pk>',
    #     views.SubjectDetailView.as_view(),
    #     name='subject_detail',
    # ),
    path('', include(router.urls)),
    # path(
    #     'courses/<int:pk>/enroll/',
    #     views.CourseEnrollView.as_view(),
    #     name='course_enroll'
    # ),
]
