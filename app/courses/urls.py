from django.urls import path
from . import views


app_name = 'courses'
urlpatterns = [
    path('mine/', views.ManageCourseListView.as_view(), name='manage-course-list'),
    path('create/', views.CourseCreateView.as_view(), name='create-course'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='update-course'),
    path('<pk>/delete/', views.CourseDeleteView.as_view(), name='delete-course'),
]