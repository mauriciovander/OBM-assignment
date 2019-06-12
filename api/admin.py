from django.contrib import admin
from .models import Member, Company

# Register your models here.
admin.site.register(Company)
admin.site.register(Member)
