from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Member
from .serializers import CompanySerializer, MemberSerializer

# Create your views here.

class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer