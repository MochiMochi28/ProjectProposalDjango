from django.db import models

# Create your models here.

class AddSections(models.Model):
    newSection=models.CharField( unique=True, max_length=20, blank=True ,default="Others")
    
    def __str__(self):
        return self.newSection