from django.db import models
from bookinfos.models import BookInfo

# Create your models here.

class BorrowedBooks(models.Model):
    studentLRN=models.IntegerField(blank=False,null=False)
    studentGLevel = models.CharField(max_length=50,blank=False ,null=False)
    studentSection = models.CharField(max_length=50,blank=False , null=False)
    dateBorrowed = models.DateField( blank=False ,default="2024-12-09")
    dateReturned = models.DateField( blank=False ,default="2024-12-09")
    # bookNumber=models.IntegerField(blank=False, null=False)
    book=models.ForeignKey(BookInfo,  on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.studentLRN} ,{ self.studentGLevel} ,{self.studentSection}, {self.book}"



