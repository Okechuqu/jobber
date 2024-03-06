from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login/')
def dashboard(request, pagename=None):
    context = {}

    if (pagename) and (pagename != 'index') and not (str(pagename)).__contains__('.html'):
        return render(request, f'{pagename}.html', context=context)

    return render(request, 'dashboard/dashboard.html', context=context)