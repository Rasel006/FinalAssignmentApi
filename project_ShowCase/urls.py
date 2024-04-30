from django.urls import path, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()

router.register('list', views.ProjectDetailsViewSet)
router.register('Project-Image', views.ProjectImageViewSet)
router.register('Project-Tech-Stack', views.TechStakViewSet)
router.register('Categoty', views.CategoryViewSet)
router.register('Project-Review', views.RatingsViewSet)

urlpatterns = [
    path('', include(router.urls))
]