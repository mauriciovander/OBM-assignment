from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)    
    address = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    
    def __str__(self):
        return self.name
    

class Member(models.Model): 
    firstname = models.CharField(max_length=100)   
    infix = models.CharField(max_length=20, blank=True)    
    lastname = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=50, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    photo = models.URLField(blank=True)

    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)
    
    @property
    def company_name(self):
        return self.company.name

    @property
    def company_address(self):
        return self.company.address

    @property
    def company_photo(self):
        return self.company.photo
