from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    STATUS = (
        (1, 'doctor'),
        (2, 'reception'),
        (3, 'patient')
    )
    specialist = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    qualification = models.IntegerField(null=True, blank=True)
    types = models.IntegerField(choices=STATUS,default=1)


class Category(models.Model):
    name = models.CharField(max_length=255)



class RegisterPatient(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    age = models.IntegerField()
    injury = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    doctorname = models.ForeignKey(User,on_delete=models.CASCADE)
    payment = models.IntegerField()


class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()


class AnalysisPatient(models.Model):
    STATUS = (
        (1, 'is injury'),
        (2, 'is healthy'),
    )
    DAVO = (
        (1, 'uyda'),
        (2, 'shifoxonada'),
    )
    patient = models.ForeignKey(RegisterPatient,on_delete=models.CASCADE)
    is_injury = models.IntegerField(choices=STATUS, default=1)
    injurytype = models.CharField(max_length=255,null=True, blank=True)
    pharmacy = models.ForeignKey(Pharmacy,on_delete=models.CASCADE,related_name='dorixona',null=True, blank=True)
    quantitymedicine = models.IntegerField(null=True, blank=True)
    typetreatment = models.IntegerField(choices=DAVO,default=2,null=True, blank=True)
    daytreat = models.IntegerField(null=True, blank=True)



class Info(models.Model):
    hospitalname = models.CharField(max_length=255)
    phone = models.IntegerField()
    adress = models.CharField(max_length=255)
    workinghour = models.IntegerField()
    dayoff = models.CharField(max_length=255, null=True, blank=True)

#   NULL TRUE BERAMZ ANALIZGA

