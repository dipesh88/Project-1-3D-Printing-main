from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm, PartUploadForm
from .util import *

# Create your views here.

def home(request):
    return render(request,'get_print/home.html')

def about(request):
    return render(request, 'get_print/about.html')

# Ask for user registration details and save it in database.
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('workspace')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="get_print/register.html", context={"register_form":form})

# Verify credentials and login user
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('workspace')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name='get_print/login.html', context={'login_form':form})

# Logout user
@login_required
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

# User's workspace: Parts, orders, history, profile.
@login_required
def workspace(request):
    return render(request, 'get_print/workspace.html')

# Show all parts Consumer has uploaded
@login_required
def parts(request):
    parts = request.user.consumer.parts.all()
    return render(request, 'get_print/parts.html', {'parts': parts})

# Lets user upload the model to print
@login_required
def upload_part(request):
    if request.method == 'POST':
        uploaded_part = PartUploadForm(request.POST, request.FILES)
        if uploaded_part.is_valid():
            p = uploaded_part.save()
            request.user.consumer.parts.add(p)
            return redirect('parts')
    form = PartUploadForm()
    return render(request, 'get_print/upload_part.html', {'part_upload_form': form})
