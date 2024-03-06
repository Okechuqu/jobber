from django.urls import path
from .views import *


urlpatterns = [
    path('update-company/', update_company, name="update-company"),
    path('details/<int:pk>/', company_details, name="details")
]
