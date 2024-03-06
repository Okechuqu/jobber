from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('all-jobs/', job_listing, name='all-jobs'),
    path('job-details/<int:pk>/', job_details, name='job-details')
]
