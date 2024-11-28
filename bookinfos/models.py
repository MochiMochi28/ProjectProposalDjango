from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookInfo(models.Model):
    
    bookTitle = models.CharField(max_length=50,blank=False , null=False)
    author = models.CharField(max_length=50 , blank=False , null=False)
    datePublished = models.DateField( blank=False , null=False)
    bookNumber=models.IntegerField(blank=False,null=False)
    quantity=models.IntegerField(blank=False, )
    sections=models.CharField( max_length=20, blank=False ,default="Others")

    def __str__(self):
        return f"{self.bookTitle} ,{ self.author} , {self.bookNumber}"

