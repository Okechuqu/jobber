from django.urls import path
from .views import *


urlpatterns = [
    path('update-resume/', update_resume, name="update-resume"),
    path('resume-details/<int:pk>/', resume_details, name="resume-details")
]
