from django.db import models


class UserData(models.Model):
    """Model Class for user information"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    profile_image = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.email

        