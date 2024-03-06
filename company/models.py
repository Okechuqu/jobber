from django.db import models
from users.models import User

# Create your models here.


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    est_date = models.PositiveIntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    # insert cv

    def __str__(self):
        return self.company_name
