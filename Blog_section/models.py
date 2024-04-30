from django.db import models

# Create your models here.
class BlogModel(models.Model):
    Publisher_name = models.CharField(max_length=50)
    Title = models.CharField(max_length=150)
    body = models.TextField()
    
    def __str__(self) -> str:
        return f"The Blog Writen By {self.Publisher_name}"
    