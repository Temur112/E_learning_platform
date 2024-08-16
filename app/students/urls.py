from django.urls import path
from . import views


app_name = 'students'
urlpatterns = [
    path('register/', views.StudentRegistrationForm.as_view(), name='student_registration'),
]