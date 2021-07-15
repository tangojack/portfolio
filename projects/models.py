from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(blank=True, null=True, upload_to="cover_images/")
    def __str__(self):
        return self.title
