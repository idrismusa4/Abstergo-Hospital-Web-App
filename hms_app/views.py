from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from hms_app.forms import patient_registration_form
# from .forms import PatientRegistrationForm, PatientLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test



def index(request):
    return render(request, 'templates/index.html')

def genappointmentschedule(request):
    return render(request, 'templates/generalappointmentschedule.html')

def doctorlogin(request):
    return render(request, 'templates/stafflogin.html')

def doctorappointmentschedule(request):
    return render(request, 'templates/doctorappointmentschedule.html')

def contactuspage(request):
    return render(request, 'templates/Contact us Page.html')




def adminlogin(request):
        if request.method == "POST":
            username = request.POST ['username']
            password = request.POST ['password']

            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')
                #Success

            else:
                messages.success(request, 'Invalid Username or Password,Try Again')
                return redirect('adminlogin')
            #invalid credentials


        else:

            return render(request, 'templates/adminlogin.html')

def patientcontactus(request):
    return render(request, 'templates/patientcontactus.html')

def patientappointmentschedule(request):
    
    return render(request, 'templates/patient-appointment-schedule.html')

def patientregistration(request):
    if request.method == "POST":
        form = patient_registration_form(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'You Have Been Registered Successfully!')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You Have Been Registered Successfully!')
            return redirect('patientlogin')
        elif User.objects.filter(username=form.cleaned_data['username']).exists():
            messages.success(request, 'Username Already Exists!')
            return redirect('patient_registration')

    else:
        form = patient_registration_form()
    return render(request, 'templates/patient-registration.html', {'form': form})


def patientlogin(request):
    if request.method == "POST":
        username = request.POST ['username']
        password = request.POST ['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('patient_dashboard')
            #Success

        else:
            messages.success(request, 'Invalid Username or Password,Try Again')
            return redirect('patientlogin')
        #invalid credentials


    else:
        return render(request, 'templates/patientlogin.html')

def admin_logout(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out!')
    return redirect('index')

def patient_logout(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out!')
    return redirect('index')

def staff_logout(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out!')
    return redirect('index')

def patientindex(request):
    return render(request, 'templates/patient-index.html')




def patientdashboard(request):
    return render(request, 'templates/patient-dashboard.html')

def doctordashboard(request):
    return render(request, 'templates/staff-dashboard.html')

def staffindex(request):
    return render(request, 'templates/staffindex.html')

def patientbooking(request):
    return render(request, 'templates/patientbooking.html')

def edit_patient_profile(request):
    return render(request, 'templates/edit-patient-profile.html')

def admindashboard(request):
    return render(request, 'templates/admin_dashboard.html')


def create_appointment(request):
    pass