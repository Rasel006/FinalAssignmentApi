from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.
class SkillsViewSet(viewsets.ModelViewSet):
    queryset = models.SkillsModel.objects.all()
    serializer_class = serializers.SkillsSerializers

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = models.Resume.objects.all()
    serializer_class = serializers.ResumeSerializers