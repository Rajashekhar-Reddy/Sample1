from django.db import models

# Create your models here.
class student(models.Model):
    
    sname=models.CharField(max_length=30)
    slname=models.CharField(max_length=30)
    scountry=models.CharField(max_length=30)
    semail=models.EmailField(max_length=50)
    susername=models.CharField(max_length=50)
    spassword=models.SlugField(max_length=50)
    snumber=models.IntegerField()
    sgender = models.CharField(max_length=128)
    sdob=models.CharField(max_length=50)
    squalification=models.CharField(max_length=50)
    sadress=models.SlugField(max_length=50)
   
    
    
