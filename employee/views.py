from urllib import response
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.postgres.search import (
    SearchQuery,
    SearchVector,
    SearchRank,
)

from employee.models import Employee, Company
from employee.serializers import (
    CompanySerializer,
    EmployeeSerializer,
    EmployeeListSerializer
)


# Company views
class CompanyCreateAPIView(generics.CreateAPIView):
    """
    View to create company
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Company created successfully!',
            'data': response.data
        })
    

class CompanyListAPIView(generics.ListAPIView):
    """
    View to list out all companies
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetailAPIView(generics.RetrieveAPIView):
    """
    View to retrive company instance
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # lookup_field = 'pk' # Default setting


class CompanyUpdateAPIView(generics.UpdateAPIView):
    """
    View to update company instance
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Company updated successfully!',
            'data': response.data
        })

class CompanyDeleteAPIView(generics.DestroyAPIView):
    """
    View to delete company instance
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)    
        return Response({
            'status': 200,
            'message': 'Company deleted successfully!',
            'data': response.data
        })


# Employee views
class EmployeeCreateAPIView(generics.CreateAPIView):
    """
    View to create employee
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Employee created successfully!',
            'data': response.data
        })
        

class EmployeeListAPIView(generics.ListAPIView):
    """
    View to list all employees and filtering company employee 
    """
    serializer_class = EmployeeListSerializer
    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        """
        If company present in query params return all employee 
        of that company. Else return all employee
        """
        company = self.request.query_params.get('company')
        if company is not None:
            queryset = Employee.objects.filter(company__name__contains=company)
            print(queryset)
            return queryset
        
        queryset = Employee.objects.all()
        return queryset
    

class EmployeeFullTextSearchAPIView(generics.ListAPIView):
    """
    View for full text search
    """
    serializer_class = EmployeeListSerializer
    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search is not None:
            # using full text search 
            vector = SearchVector('job_title')
            query = SearchQuery(search)

            queryset = Employee.objects.annotate(rank=SearchRank(vector,query)).order_by("-rank")
            return queryset

        queryset = Employee.objects.all()
        return queryset 