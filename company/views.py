from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import UpdateCompanyForm
from users.models import User


# Create your views here.
# Update company details
@login_required(login_url=('/login/'))
def update_company(request):
    if request.user.is_recruiter:
        company = Company.objects.get(user=request.user)
        if request.method == 'POST':
            form = UpdateCompanyForm(request.POST, instance=company)
            if form.is_valid:
                data = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                user.has_company = True
                user.save()
                data.save()
                messages.info(request, 'Your Company is Active, you should create Job ads!!!')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went Wrong')
            
        else:
            form = UpdateCompanyForm(instance=company)
            context = {'form': form}
            return render(request, 'company/update-company.html', context)
    else:
        messages.warning(request,'Not Allowed')
        return redirect('dashboard')



# view Details
@login_required(login_url=('/login/'))
def company_details(request, pk):
    company = Company.objects.get(pk=pk)
    context = {'company':company}
    return render(request, 'company/details.html', context)