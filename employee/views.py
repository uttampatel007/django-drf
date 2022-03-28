from rest_framework import generics
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


class CompanyDeleteAPIView(generics.DestroyAPIView):
    """
    View to delete company instance
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    

# Employee views

class EmployeeCreateAPIView(generics.CreateAPIView):
    """
    View to create employee
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


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
            vector = SearchVector('job_title')
            query = SearchQuery(search)

            queryset = Employee.objects.annotate(rank=SearchRank(vector,query)).order_by("-rank")
            # queryset = Employee.objects.filter(first_name__search=search)
            return queryset

        queryset = Employee.objects.all()
        return queryset 