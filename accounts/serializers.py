from . models import User
from rest_framework import serializers
from django.auth.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'is_verified']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'role', 'password1','password2']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self,attrs):   
        if attrs['password1']!= attrs['password2']:
            raise serializers.ValidationError("passwords do not match")

        password = attrs['password1']
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")   
        return attrs 

    def create(self,validated_data):
       password = validated_data.pop('password1')
       validated_data.pop('password2')

       user = User.objects.create_user(**validated_data, password=password)
       return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)    


    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials or inactive user.")