from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)    
    address = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    # photo = models.FileField(upload_to= )
    
    def __str__(self):
        return self.name
    

class Member(models.Model): 
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # owner = models.ForeignKey('auth.User', related_name='Member', on_delete=models.CASCADE)
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

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

