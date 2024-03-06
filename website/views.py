from django.shortcuts import render, redirect
from job.models import *
from .filters import JobFilter
# Create your views here.


def index(request, pagename=None):
    context = {}

    if (pagename) and (pagename != 'index') and not (str(pagename)).__contains__('.html'):
        return render(request, f'{pagename}.html', context=context)

    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    filters = JobFilter(request.GET, queryset=jobs)
    context = {'filters':filters}

    return render(request, 'website/index.html', context=context)


def job_listing(request):
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    context = {'jobs':jobs}
    return render(request, 'website/all-jobs.html', context)


def job_details(request, pk):
    data = ApplyJob.objects.filter(user=request.user, job=pk).exists()
    if data:
        has_applied = True
    else:
        has_applied = False
    job = Job.objects.get(pk=pk)
    context= {'job':job, 'has_applied':has_applied}
    return render(request, 'website/job-details.html', context)