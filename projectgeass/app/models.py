from django.db import models

# Create your models here.

class Post(models.Model):
   text = models.TextField(max_length=256)
   time = models.DateTimeField(auto_now_add=True)
   title = models.CharField(max_length=128)
   
   def __unicode__(self):
        return self.title   
  # user
