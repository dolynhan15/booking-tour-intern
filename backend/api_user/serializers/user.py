from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=30, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        pw = attrs.get('password', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email', 'Email is already in use'})
        elif len(pw) < 8:
            raise serializers.ValidationError({'password', 'Password must be at least 8 characters'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=30, write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, attrs):
        email = attrs.get('username', '')
        password = attrs.get('password')
        if not email:
            raise AuthenticationFailed('Invalid credentials, try again')
        elif len(password) < 8:
            raise serializers.ValidationError({'password', 'Password must be at least 8 characters'})
        return super().validate(attrs)
