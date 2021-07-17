from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(blank=True, null=True, upload_to="cover_images/", default="cover_images/default.jpeg")
    url = models.URLField(blank=True, null=True)

    @property
    def cover_image_url(self):
        if self.cover_image and hasattr(self.cover_image, 'url'):
            return self.cover_image.url

    def __str__(self):
        return self.title
