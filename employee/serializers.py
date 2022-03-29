from rest_framework import serializers
from employee.models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
    """Model serializer for company"""
    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    """Model serializer for employee"""
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeListSerializer(serializers.ModelSerializer):
    """Model serializer for employee"""
    company_name = serializers.CharField(source='company.name')
    class Meta:
        model = Employee
        fields = [
            "email",
            "full_name",
            "company_name",
            "gender",
            "job_title",
            "total_experience",
            "avatar"
        ]