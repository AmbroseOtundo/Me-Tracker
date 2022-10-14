from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Medicine


def index(request):
    return render(request, 'Tracker/index.html')

def homepage(request):
    return render(request, 'Dashboard/base.html')

# Register
def register_request(request):
    if request.method == 'GET':
        return render(request, 'Tracker/register.html', {'form':UserCreationForm()})
    else:
        # match password
        if request.POST['password1'] == request.POST['password2']:
        # create a new user
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'] )
                user.save()
                login(request, user)
                messages.success(request, "Sign up succcesful" )
                return redirect('Dashboard/base.html')
            except IntegrityError:
                return render(request, 'Tracker/register.html', {'form':UserCreationForm(), 'error':'That username is already taken, please choose another one'})
 
        else:
            # tell user pass did not match
            return render(request, 'Tracker/register.html', {'form':UserCreationForm(), 'error':'Passwords do not match'})

# Login
def loginuser(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('homepage')
			else:
				messages.error(request,'Invalid username or password.')
		else:
			messages.error(request,'Invalid username or password.')
	form = AuthenticationForm()
	return render(request=request, template_name="Tracker/login.html", context={"login_form":form})



@login_required
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

def my_dosage_list(request):
    # Getting the medicine object that belongs to the user.
    dosage_lists = Medicine.objects.exclude(user=request.user)
    return render(request, "Dashboard/dosage_list.html", {"dosage_lists": dosage_lists})
