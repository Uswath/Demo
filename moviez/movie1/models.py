from django.db import models

# Create your models here.
class movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    img = models.ImageField(upload_to='moviez/img', null=True, blank=True)