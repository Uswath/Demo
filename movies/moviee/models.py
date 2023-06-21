from django.db import models


# Create your models here.
class movies(models.Model):
    cover = models.ImageField(upload_to='moviee/cover', null=True, blank=True)
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=400)
