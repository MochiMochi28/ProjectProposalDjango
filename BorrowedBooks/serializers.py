from rest_framework import serializers
from bookinfos.serializers import BookInfoSerializer
from .models import BorrowedBooks
from bookinfos.models import BookInfo

class BorrowedBooksSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=BookInfo.objects.all())
    class Meta:
        model=BorrowedBooks
        fields = ['id' , 'studentLRN', 'studentGLevel', 'studentSection', 'dateBorrowed', 'dateReturned','book']
        depth=1
        
class GetBookSerializer(serializers.ModelSerializer):
     class Meta:
        model=BorrowedBooks
        fields = ['id' , 'studentLRN', 'studentGLevel', 'studentSection', 'dateBorrowed', 'dateReturned','book']
        depth=1