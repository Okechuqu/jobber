from django.urls import path
from . import views

urlpatterns = [
    path('register-applicants/', views.register_applicants,
         name='register-applicants'),
    path('register-recruiter/', views.recruiter_register,
         name='register-recruiter'),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
]
