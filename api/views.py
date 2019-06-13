from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Company, Member
from .serializers import CompanySerializer, MemberSerializer
import django_filters
from django.contrib.auth.models import User

class CompanyView(viewsets.ModelViewSet):

    def get_queryset(self):
        user = self.request.user 
        if(str(user)=='AnonymousUser'):
            return Company.objects.filter(id=-1)

        if(user.is_staff):
            queryset = Company.objects.all()
        else:
            company_id = Member.objects.filter(username=user.username)[0].company.id
            queryset = Company.objects.filter(id=company_id)
        return queryset

    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
    search_fields = ('name','address', )
    ordering_fields = '__all__'

    
class MemberView(viewsets.ModelViewSet):

    def get_queryset(self):
        user = self.request.user
        # TODO: Create filter based on authenticated user
        # user.staff = True
        # user.admin = True
        if(str(user)=='AnonymousUser'):
            return Member.objects.filter(id=-1)

        if(user.is_staff):
            queryset = Member.objects.all()
        else:
            company = Member.objects.filter(username=user.username)[0].company
            queryset = Member.objects.filter(company=company)
        return queryset


    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
    search_fields = ('last_name','first_name', )
    ordering_fields = '__all__'
