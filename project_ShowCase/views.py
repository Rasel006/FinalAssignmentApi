from django.shortcuts import render
from django.db.models import Avg
from rest_framework import viewsets,filters, pagination
from . import models
from . import serializers
# Create your views here.
class ProjectPagination(pagination.PageNumberPagination):  
    page_size = 6
    page_size_query_param = page_size
    max_page_size = 100

class AvailableProjectsForCategory(filters.BaseFilterBackend):
     def filter_queryset(self, request, query_set, view):
        Category_id = request.query_params.get("category_id")
        if Category_id:
            return query_set.filter(category = Category_id)
        return query_set

class ProjectDetailsViewSet (viewsets.ModelViewSet):
    queryset = models.ProjectDetailsModel.objects.annotate(avg_rating=Avg('ratings__rating')).order_by('-avg_rating')
    serializer_class = serializers.ProjectDetailsSerializer
    pagination_class = ProjectPagination
    filter_backends = [AvailableProjectsForCategory]

class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectImage.objects.all()
    serializer_class = serializers.ProjectImageSerializer
  
class TechStakViewSet(viewsets.ModelViewSet):
    queryset = models.TechStack.objects.all()
    serializer_class = serializers.TechStackSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
  
class RatingsViewSet(viewsets.ModelViewSet):
    queryset = models.Ratings.objects.all()
    serializer_class = serializers.RatingSerializer
  