from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

class blogViewSet(viewsets.ModelViewSet):
    queryset = models.BlogModel.objects.all()
    serializer_class = serializers.BlogSerializer