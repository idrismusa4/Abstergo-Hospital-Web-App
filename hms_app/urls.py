from django.urls import path
from hms_app import views
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path ('generalappointmentschedule/', views.genappointmentschedule, name='generalappointmentschedule'),
    path ('stafflogin/',views.doctorlogin, name='doctorlogin'),
    path ('doctorappointmentschedule/',views.doctorappointmentschedule, name='doctorappointmentschedule'),
    path ('Contact us Page/', views.contactuspage, name='contactuspage'),
    path ('adminlogin/',views.adminlogin,name='adminlogin'),
    path ('patientcontactus/', views.patientcontactus, name='patientcontactus'),
    path ('patient-appointment-schedule/', views.patientappointmentschedule,name='patientappointmentschdule'),
    path ('patientlogin/', views.patientlogin,name='patientlogin'),
    path ('patient_logout/', views.patient_logout,name='patient_logout'),
    path ('admin_logout/', views.admin_logout,name='admin_logout'),
    path ('patient-index/',views.patientindex,name='patientindex'),
    path ('patient-dashboard/', views.patientdashboard, name='patient_dashboard'),
    path ('staff-dashboard/', views.doctordashboard, name='doctor_dashboard'),
    path ('staffindex/', views.staffindex, name='staff_index'),
    path ('patient-registration/', views.patientregistration, name='patient_registration'),
    path ('edit-patient-profile/', views.edit_patient_profile,name='editprofile'),
    path ('admin_dashboard/', views.admindashboard, name='admin_dashboard'),
    path ('create_appointment/', views.create_appointment, name='create_appointment'),
]
