from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *


# Create your views here.
@login_required
def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreateJobForm(request.POST)
            if form.is_valid:
                data = form.save(commit=False)
                data.user = request.user
                data.company = request.user.company
                data.save()
                messages.info(request,'Job Created !!!')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something Went Wrong')
                return redirect('create-job')
        else:
            form = CreateJobForm()
            context = {'form':form}
            return render(request, 'job/create-job.html', context)
    else:
        messages.warning(request, 'Not Allowed, Create a Company')
        return redirect('dashboard')

# update job
@login_required
def update_job(request, pk):
    if request.user.is_recruiter and request.user.has_company:
        job = Job.objects.get(pk=pk)
        if request.method == 'POST':
            form = UpdateJobForm(request.POST, instance=job)
            if form.is_valid:
                form.save()
                messages.info(request,'Job Info Updated !!!')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something Went Wrong')
        else:
            form = UpdateJobForm(instance=job)
            context = {'form':form}
            return render(request, 'job/update-job.html', context)
    else:
        messages.warning(request, 'Not Allowed, Create a Company')
        return redirect('dashboard')


def manage_job(request):
    if request.user.is_recruiter and request.user.has_company:
        jobs = Job.objects.filter(user=request.user, company=request.user.company)
        context = {'jobs':jobs}
        return render(request, 'job/manage-job.html', context)
    else:
        messages.warning(request, 'Not Allowed, Create a Company')
        return redirect('dashboard')

 
def apply_job(request, pk):
    if request.user.is_authenticated and request.user.is_applicant and request.user.has_resume:
        job = get_object_or_404(Job, pk=pk)
        data = ApplyJob.objects.filter(user=request.user, job=pk).exists()
        if data:
            messages.warning(request, 'Already Applied')
            return redirect('all-jobs')
        else:
            ApplyJob.objects.create(
                job=job,
                user=request.user,
                status = 'Pending'
            )
            messages.info(request, 'Applied Successfuly, Wait for Feedback')
            return redirect('dashboard')
    else:
        messages.warning(request, 'Login Fess')
        return redirect('login')


def all_applicants(request, pk):
    job = get_object_or_404(Job, pk=pk)
    applicants = job.applyjob_set.all()
    context = {'job':job, 'applicants':applicants}
    return render(request, 'job/all-applicants.html', context)


def applied_jobs(request):
    jobs = ApplyJob.objects.filter(user=request.user)
    context = {'jobs':jobs}
    return render(request, 'job/applied-jobs.html', context)

