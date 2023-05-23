from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100,default='')
    email = models.EmailField()
    phone_no = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name



class Appointments(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    reasonforappointment = models.TextField(max_length=100,default='')

    def __str__(self):
        return self.patient.name + ' - ' + self.doctor.name

