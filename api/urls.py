from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views
# from .views import api_home


urlpatterns = [
    path('auth/', obtain_auth_token),
    path('user/', views.UserCreateAPIView.as_view()),
    path('user/<int:pk>/', views.UserDetailAPIView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateAPIView.as_view()),
    path('user/<int:pk>/delete/', views.UserDeleteAPIView.as_view()),
    path('user/list/', views.UserDetailListAPIView.as_view()),
]