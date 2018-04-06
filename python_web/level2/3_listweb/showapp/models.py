from django.db import models

# Create your models here.
class waterfall(models.Model):
    name = models.CharField(null=True,blank=True,max_length=200)
    img = models.CharField(null=True,blank=True,max_length=200)
    like_num = models.CharField(null=True,blank=True,max_length=200)
    got_num = models.CharField(null=True,blank=True,max_length=200)

    def __str__(self):
        return self.img