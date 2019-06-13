from rest_framework import serializers
from .models import Company, Member
from django.contrib.auth.models import User

# class CompanySerializer(serializers.HyperlinkedModelSerializer):
class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'address', 'photo')


# class MemberSerializer(serializers.HyperlinkedModelSerializer):
class MemberSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = Member.objects.create_user(**validated_data)
        return user       

    company_name = serializers.ReadOnlyField()
    company_photo = serializers.ReadOnlyField()
    company_address = serializers.ReadOnlyField()

    class Meta:
        model = Member
        fields = ('id', 'username', 'password', 'first_name', 'infix', 'last_name', 'jobtitle', 'photo', 'company', 'company_name','company_address', 'company_photo')
        extra_kwargs = {
            'password': {'write_only': True}
        }
