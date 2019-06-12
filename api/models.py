from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)    
    address = models.TextField()
    
    def __str__(self):
        return self.name
    

class Member(models.Model):
    firstname = models.CharField(max_length=100)    
    lastname = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)
    
    

    