from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from api_users.serializers import *
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# USERS VIEWS
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    

class ChangePassword(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def put(self, request, pk):
        password = request.data['password']
        new_password = request.data['new_password']

        user = User.objects.filter(id=pk).first()
        if not user.check_password(raw_password=password):
            return Response({'error': 'password not match'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.set_password(new_password)
            user.save()
            return Response({'success': 'password changed successfully'}, status=status.HTTP_200_OK)
    

class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(is_active=True)
    
    def delete(self, request, pk=None):
        user = self.get_queryset().filter(id=pk).first()
        if user:
            user.is_active = False
            user.save()
            return Response({"message": "User has been desactivated sucessfully!"}, status=status.HTTP_200_OK)
        
        return Response({"message": "User not found!"}, status=status.HTTP_400_BAD_REQUEST)        


# LOGIN AND LOGOUT
class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(
            username = username,
            password = password
        )
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid() and user.is_active:
                user_serializer = UserSerializer(user)
                return Response({
                    "token":f"Bearer {login_serializer.validated_data['access']}",
                    "refresh_token": login_serializer.validated_data['refresh'],
                    "user": user_serializer.data,
                    "message": "Login sucessfull!"
                }, status=status.HTTP_200_OK)
            return Response({"error": "User is invalid to login!"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"error": "Password, Username wrong or User is invalid!"}, status=status.HTTP_400_BAD_REQUEST)
    
class Logout(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        
        print(request.headers)
        print(request.data)
        user = User.objects.filter(id=request.data.get('user', 0))

        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        return Response({"error": "User does not exist!"}, status=status.HTTP_400_BAD_REQUEST) 