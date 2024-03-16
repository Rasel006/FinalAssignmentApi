from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
class RegistationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if  password != confirm_password:
            raise serializers.ValidationError({'erro': "Password doesn't match"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"Email Already Exists"})
        
        else:
            account = User(username=username, email=email,first_name=first_name, last_name = last_name)
            account.set_password(password)
            account.is_active = False
            account.save()
            print(account)
            return account
class userLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

class alluserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'

class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name']

    def update(self, instance,validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance

class UpdateProfileImage(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileImage
        fields = ['profile_image']
    