from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# @login_required
def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'broadcast.html')

def about(request):
    return render(request, 'about.html')

# Temporary Report sheet page
def reportsheet(request):
    return render(request, 'reportsheet.html')
    
@login_required(login_url='login')
def success(request):
    return HttpResponse("Success")