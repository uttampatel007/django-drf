from rest_framework import generics, authentication, permissions

from users.models import UserData
from users.serializers import UserDataSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     
    #     serializer.save(user=request.user)
    #     # or send a Django signal


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    # lookup_field = 'pk' ??


class UserDetailListAPIView(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    # lookup_field = 'pk'

    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     pass

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    
    # def perform_destroy(self, instance):
    #     return super().perform_destroy(instance)



# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from users.serializers import UserDataSerializer
# from users.models import UserData


# @api_view(["GET"])
# def get_users_api(request, *args, **kwargs):
#     """Django REST api"""

#     instance = UserData.objects.first()
#     data = {}
#     data = UserDataSerializer(instance).data

#     return Response(data)


# @api_view(["POST"])
# def post_users_api(request, *args, **kwargs):
#     """Django REST api"""

#     instance = UserData.objects.first()
#     data = {}
#     data = UserDataSerializer(instance).data

#     return Response(data)
