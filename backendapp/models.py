from django.db import models

# Create your models here.

class categorydb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="profile",null=True,blank=True)
    Descript=models.CharField(max_length=1000,null=True,blank=True)

class sectiondb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="profile",null=True,blank=True)
    Descript=models.CharField(max_length=1000,null=True,blank=True)
    category=models.CharField(max_length=100,null=True,blank=True)

