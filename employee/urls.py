from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from employee import views


urlpatterns = [
    # user auth urls
    path('auth/', obtain_auth_token),

    # company api urls
    path("company/", views.CompanyCreateAPIView.as_view(), name="create-company"),
    path("company/list/", views.CompanyListAPIView.as_view(), name="list-company"),
    path("company/<int:pk>/", views.CompanyDetailAPIView.as_view(), name="get-company"),
    path("company/<int:pk>/update/", views.CompanyUpdateAPIView.as_view(), name="update-company"),
    path("company/<int:pk>/delete/", views.CompanyCreateAPIView.as_view(), name="delete-company"),

    # employee api urls
    path("employee/", views.EmployeeCreateAPIView.as_view(), name="create-employee"),
    path("employee/list/", views.EmployeeListAPIView.as_view(), name="list-employee"),
    path("employee/fts/", views.EmployeeFullTextSearchAPIView.as_view(), name="full-text-search-employee"),

]