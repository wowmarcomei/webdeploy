from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(null=True,blank=True, max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.name