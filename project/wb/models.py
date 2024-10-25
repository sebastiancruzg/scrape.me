from django.db import models

# Create your models here.

class Resource(models.Model):
    tag = models.CharField(max_length=50)
    url = models.URLField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.tag
