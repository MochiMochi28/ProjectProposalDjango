from rest_framework import serializers

from .models import BookInfo

class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'
        # fields = ['id','bookTitle', 'author' , 'datePublished','bookNumber', 'quantity', 'sections']