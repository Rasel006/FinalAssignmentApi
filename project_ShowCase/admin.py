from django.contrib import admin
from . models import Category,ProjectDetailsModel, ProjectImage, Ratings,TechStack
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']

admin.site.register(Category,CategoryAdmin)
admin.site.register(ProjectDetailsModel)
admin.site.register(ProjectImage)
admin.site.register(Ratings)
admin.site.register(TechStack)