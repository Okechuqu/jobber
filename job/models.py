from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
from company.models import Company



# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.name
    
class Industry(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    job_type_choices = (
        ('Remote','Remote'),
        ('Onsite','Onsite'),
        ('Hybrid','Hybrid'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    salary = models.PositiveIntegerField(default=35000)
    requirements = models.TextField()
    ideal_candidate = models.TextField()
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    industry = models.ForeignKey(Industry, on_delete=models.DO_NOTHING,blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING,blank=True, null=True)
    job_type = models.CharField(max_length=20, choices=job_type_choices ,blank=True, null=True)
    
    class Meta:
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Job_detail", kwargs={"pk": self.pk})


class ApplyJob(models.Model):
    status_options = (
        ('Approved','Approved'),
        ('Declined','Declined'),
        ('Pending','Pending'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_options)

    class Meta:
        verbose_name = _("ApplyJob")
        verbose_name_plural = _("ApplyJobs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Job_detail", kwargs={"pk": self.pk})

