import os

import requests
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from ..models import User, UserProfile
from ..serializers.user import UserSerializer, LoginSerializer, UserProfileSerializer
from dotenv import load_dotenv

load_dotenv()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterAPIView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            r = requests.post(
                'http://127.0.0.1:8000/o/token/',
                data={
                    'grant_type': 'password',
                    'username': request.data['username'],
                    'password': request.data['password'],
                    'client_id': os.environ.get('CLIENT_ID'),
                    'client_secret': os.environ.get('CLIENT_SECRET'),
                },
            )
            response = r.json()
            response.update(serializer.data)
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
