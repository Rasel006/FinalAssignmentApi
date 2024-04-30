from rest_framework import serializers
from . import models

class SkillsSerializers(serializers.ModelSerializer):
    class Meta: 
        model = models.SkillsModel
        fields = '__all__'
        
class ResumeSerializers(serializers.ModelSerializer):
    class Meta: 
        model = models.Resume
        fields = '__all__'