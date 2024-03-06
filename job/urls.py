from django.urls import path
from .views import *

urlpatterns = [
    path('manage-job', manage_job, name='manage-job'),
    path('create-job/', create_job, name='create-job'),
    path('applied-jobs/', applied_jobs, name='applied-jobs'),
    path('update-job/<int:pk>/', update_job, name='update-job'),
    path('apply-job/<int:pk>/', apply_job, name='apply-job'),
    path('all-applicants/<int:pk>/', all_applicants, name='all-applicants'),
]
