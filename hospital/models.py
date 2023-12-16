from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=60)
    Mobile = models.IntegerField()
    Specialization = models.CharField(max_length=60)
    AvailableDays = models.CharField(max_length=60)
    
    def __str__(self):
        return self.Name

class Patient(models.Model):
    Name = models.CharField(max_length=60)
    Gender = models.CharField(max_length=40)
    Mobile = models.CharField(max_length=10,null=True,blank=True)
    Address = models.TextField()

    def __str__(self):
        return self.Name



class Appointment(models.Model):
    Doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()

    def __str__(self):
        return self.Doctor.Name + "__"+self.Patient.Name
