from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from users.models import User

# Create your views here.
@login_required
def update_resume(request):
    if request.user.is_applicant:
        resume = Resume.objects.get(user=request.user)
        if request.method == 'POST':
            form = UpdateResumeForm(request.POST, request.FILES, instance=resume)
            if form.is_valid():
                data = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                user.has_resume = True
                user.save()
                data.save()
                messages.info(request, 'Resume created Successfully, Apply for jobs')
                return redirect('dashboard')
            
            else:
                messages.warning(request, 'Invalid Form')
            
        else:
            form = UpdateResumeForm(instance=resume)
            context = {'form':form}
            return render(request, 'resume/update-resume.html', context)

    else:
        messages.warning(request, 'Not Allowed')
        return redirect('dashboard')

# view resume
@login_required
def resume_details(request, pk):
    resume = Resume.objects.get(pk=pk)
    context ={'resume':resume}
    return render(request, 'resume/resume-details.html', context)