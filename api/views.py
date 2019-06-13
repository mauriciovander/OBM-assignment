from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Company, Member
from .serializers import CompanySerializer, MemberSerializer
import django_filters

# Create your views here.

class CompanyView(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        print(user) #--> AnonymousUser
        return Company.objects.filter()

    # queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAdminUser, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
    search_fields = ('name','address', )
    ordering_fields = '__all__'

    
class MemberView(viewsets.ModelViewSet):
    # lookup_field = 'id'
    def get_queryset(self):
        user = self.request.user
        print(user) #--> AnonymousUser
        return Member.objects.filter()
        # return Member.objects.all().filter(company_id=user.company_id).order_by('lastname')

    # queryset = Member.objects.all().order_by('lastname')
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
    search_fields = ('lastname','firstname', )
    ordering_fields = '__all__'

## http://127.0.0.1:8000/api/members/?ordering=-lastname
## http://127.0.0.1:8000/api/members/?search=a