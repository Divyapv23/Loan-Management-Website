from django.db import models

# Create your models here.

class enquirydb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Mail=models.EmailField(max_length=100,null=True,blank=True)
    Num=models.IntegerField(null=True,blank=True)
    Service=models.CharField(max_length=100,null=True,blank=True)

class loandb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Number=models.IntegerField(null=True,blank=True)
    Type=models.CharField(max_length=100,null=True,blank=True)
    Amount=models.IntegerField(null=True,blank=True)
    Period=models.CharField(max_length=100,null=True,blank=True)

class accountdb(models.Model):
    Prefix=models.CharField(max_length=100,null=True,blank=True)
    Firstname=models.CharField(max_length=100,null=True,blank=True)
    Lastname=models.CharField(max_length=100,null=True,blank=True)
    Dob=models.CharField(max_length=100,null=True,blank=True)
    Gender=models.CharField(max_length=100,null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)
    Address1 = models.CharField(max_length=100, null=True, blank=True)
    City=models.CharField(max_length=100, null=True, blank=True)
    State=models.CharField(max_length=100, null=True, blank=True)
    Pincode=models.IntegerField(null=True,blank=True)
    Country=models.CharField(max_length=100, null=True, blank=True)
    No=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Nominee=models.CharField(max_length=100, null=True, blank=True)
    Relation=models.CharField(max_length=100, null=True, blank=True)
    Occupation=models.CharField(max_length=100, null=True, blank=True)
    Ide=models.CharField(max_length=100, null=True, blank=True)
    Idcard=models.ImageField(upload_to="profile",null=True,blank=True)
    Account=models.CharField(max_length=100, null=True, blank=True)
    Category=models.CharField(max_length=100, null=True, blank=True)
    Image=models.ImageField(upload_to="profile",null=True,blank=True)
    Sign=models.ImageField(upload_to="profile",null=True,blank=True)


