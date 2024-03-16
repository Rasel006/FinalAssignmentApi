# models.py
from django.db import models

class ProfileImage(models.Model):
    profile_image = models.ImageField(upload_to='user/media/images/profile')