from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length = 100, unique = True, null = True, blank = True)

    def __str__(self):
        return self.name 
class TechStack(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name 

class ProjectDetailsModel(models.Model):
    Project_Title = models.CharField(max_length=50)
    Despcription = models.TextField()
    Project_Url = models.CharField(max_length=250)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    tech_stack = models.ManyToManyField(TechStack, related_name='projects')
    def __str__(self):
        return self.Project_Title
     
class ProjectImage(models.Model):
    project = models.ForeignKey(ProjectDetailsModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    def __str__(self):
            return self.project.Project_Title 


START_CHOICES = [
    ('★',1),
    ('★★',2),
    ('★★★',3),
    ('★★★★',4),
    ('★★★★★',5),
    ('★★★★★★',6),
    ('★★★★★★★',7),
]
class Ratings(models.Model):
    Project = models.ForeignKey(ProjectDetailsModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    rating = models.CharField(choices = START_CHOICES ,max_length=50)
    def __str__(self):
            return f"Rating by {self.name}"