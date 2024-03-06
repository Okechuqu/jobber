from django.db import models
from users.models import User

# Create your models here.


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    upload_resume = models.FileField(upload_to='resume', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
