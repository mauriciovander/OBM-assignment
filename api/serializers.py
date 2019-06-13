from rest_framework import serializers
from .models import Company, Member

# class CompanySerializer(serializers.HyperlinkedModelSerializer):
class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'address', 'photo')


# class MemberSerializer(serializers.HyperlinkedModelSerializer):
class MemberSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField()
    company_photo = serializers.ReadOnlyField()
    company_address = serializers.ReadOnlyField()

    class Meta:
        model =  Member
        fields = ('id', 'firstname', 'infix', 'lastname', 'jobtitle', 'photo', 'company', 'company_name','company_address', 'company_photo')
