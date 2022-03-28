from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    registered_number = models.IntegerField()
    industry = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    domain_name = models.URLField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=20)
    job_title = models.CharField(max_length=200)
    experience = models.FloatField()
    avatar = models.URLField(max_length=300)

    def total_experience(self):
        return f"{self.experience} Years"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.email