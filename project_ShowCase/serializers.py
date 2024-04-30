from rest_framework import serializers
from . import models
from django.db.models import Avg
class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectImage
        fields = ['image']

class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TechStack
        fields = ['name']


class ProjectDetailsSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    tech_stack = TechStackSerializer(many=True)

    class Meta:
        model = models.ProjectDetailsModel
        fields = ['id', 'Project_Title', 'Despcription', 'Project_Url', 'category', 'tech_stack', 'images']
    def get_average_rating(self, obj):
        return models.Ratings.objects.filter(Project=obj).aggregate(Avg('rating'))['rating__avg']
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ratings
        fields = '__all__'