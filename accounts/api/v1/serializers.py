from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=255,write_only=True)
    
    class Meta:
        model = User
        fields = ['email','username','password','password2']


    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs


    def create(self,validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password =validated_data['password'])
        return user



class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username","email"]


class LogoutSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ["refresh"]        