from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils import timezone
from django.db import models
from datetime import date
from django.db import models




class Prof(models.Model):
    First_name = models.CharField(max_length=45)
    Last_name = models.CharField(max_length=45)
    addressMail = models.EmailField(max_length=45)  
    Matricule = models.IntegerField()


class Student(models.Model):
    First_name = models.CharField(max_length=45)
    Last_name = models.CharField(max_length=45)
    addressMail = models.EmailField(max_length=45)  
    Matricule = models.IntegerField()    
