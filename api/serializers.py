from rest_framework import serializers
from .models import Company, Member

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'address')


class MemberSerializer(serializers.ModelSerializer):
    # company = CompanySerializer(many=False, read_only=True)

    class Meta:
        model =  Member
        fields = ('id', 'firstname', 'lastname', 'company')
