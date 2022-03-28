import json
from django.core.management.base import BaseCommand, CommandError
from drf_assignment.settings import BASE_DIR

from employee.models import Company, Employee



class Command(BaseCommand):
    """manage command to dump data to db from json file"""

    def handle(self, *args, **options):
        
        company_file_path = str(BASE_DIR) + "/json_data/company.json"

        with open(company_file_path, 'r') as f:
            company_json_obj = json.load(f) 
        
        if company_json_obj is not None:
            for company in company_json_obj:
                instance = Company(
                    name=company.get("name"),
                    registered_number=company.get("registered_number"),
                    industry=company.get("industry"),
                    address=company.get("address"),
                    city=company.get("city"),
                    state="Alsaka",
                    country=company.get("country"),
                    domain_name=company.get("domain_name"),
                )
                instance.save()
            
            print("Company Data Dumped!")
            
        employee_file_path = str(BASE_DIR) + "/json_data/employee.json"

        with open(employee_file_path,'r') as f:
            employee_json_obj = json.load(f)
        
        if employee_json_obj is not None:
            for employee in employee_json_obj:
                company = Company.objects.get(id=employee.get("company"))
                instance = Employee(
                    email=employee.get("email"),
                    first_name=employee.get("first_name"),
                    last_name=employee.get("last_name"),
                    company=company,
                    gender=employee.get("gender"),
                    job_title=employee.get("job_title"),
                    experience=employee.get("experience"),
                    avatar=employee.get("avatar"),
                )
                instance.save()
            
            print("Employee Data Dumped!")