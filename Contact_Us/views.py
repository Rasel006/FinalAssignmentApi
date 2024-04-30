from rest_framework import serializers, viewsets
from django.core.mail import send_mail
from .models import ContactUs  # Assuming your models.py file is in the same directory as your views.py

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'body']

class ContactUsViewSets(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def perform_create(self, serializer):
        # Save the ContactUs instance
        contact_us_instance = serializer.save()

        # Get the data from the serializer
        data = serializer.data

        # You can customize the email subject and message as per your requirements
        subject = f"New Contact Us Form Submission from {data['name']}"
        message = f"Name: {data['name']}\nEmail: {data['email']}\nMessage: {data['body']}"

        # Send the email to the admin
        send_mail(subject, message, data['email'], ['rizurasel.cse@gmail.com'])