from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.Auth_serializer import SignupSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

User = get_user_model()

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"id": user.id,"Message": "User created successfully.","Name": user.first_name}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        data = request.data
        authenticated_user = authenticate(email=data.get('email'), password=data.get('password'))
        if authenticated_user:
            refresh = RefreshToken.for_user(authenticated_user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user_id": authenticated_user.id,
                "email": authenticated_user.email,
                "first_name": authenticated_user.first_name,
                "last_name": authenticated_user.last_name,
                "profile_picture": authenticated_user.profile_picture.url if authenticated_user.profile_picture else None,
                "country": authenticated_user.country,
                "contact_number": authenticated_user.contact_number,
            }, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    


class SellerLogin(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        # Authenticate using email and password
        user = authenticate(email=email, password=password)

        # Check if authenticated and is_superuser
        if user and hasattr(user, 'is_superuser') and user.is_superuser:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user_id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }, status=status.HTTP_200_OK)

        return Response({"message": "Invalid credentials or not a seller"}, status=status.HTTP_401_UNAUTHORIZED)