from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from . import models
from . import serializers
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from rest_framework.response import Response
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
# Create your views here.


class RegisterViewSet(APIView):
    serializer_class = serializers.RegistationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print(token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print(uid)
            confirm_link = f"https://mdraselportfolioapi.onrender.com/user/active/{uid}/{token}"
            email_subject = "Confirm Your Mail"
            email_body = render_to_string('confirm_email.html', {'confirm_link':confirm_link})

            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response("Check Your Email To Confirm")
        return Response(serializer.errors)
    

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')


class UserLoginView(APIView):
    def post(self,request):
        serializer = serializers.userLoginSerializer(data=self.request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username = username, password = password)

            if user: 
                token,_ = Token.objects.get_or_create(user = user)
                print(token)
                print(_)
                login(request,user)

                return  Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': "InValid Credential"})
        return Response(serializer.errors)

class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
class UpdateUser(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UpdateUserProfileSerializer
    def get_object(self):
        return self.request.user
    
class UpdateUserProfileImage(viewsets.ModelViewSet):
    queryset = models.ProfileImage.objects.all()
    serializer_class = serializers.UpdateProfileImage

class AllUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.alluserSerializer