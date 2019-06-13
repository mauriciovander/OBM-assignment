from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Company, Member
from .serializers import CompanySerializer, MemberSerializer
import django_filters

class CompanyView(viewsets.ModelViewSet):

    def get_queryset(self):
        # TODO: Create filter based on authenticated user
        user = self.request.user      
        return Company.objects.filter()

    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAdminUser, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
    search_fields = ('name','address', )
    ordering_fields = '__all__'

    
class MemberView(viewsets.ModelViewSet):

    def get_queryset(self):
        user = self.request.user
        # TODO: Create filter based on authenticated user
        # user.staff = True
        # user.admin = True
        return Member.objects.filter() 

    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
    search_fields = ('lastname','firstname', )
    ordering_fields = '__all__'
