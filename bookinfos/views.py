from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookInfoSerializer

from rest_framework.parsers import JSONParser

# model imports
from .models import BookInfo

# Create your views here.
class bookInfoView(APIView):
    
    def get(self , request , format=None):
        data = BookInfo.objects.all().order_by('-id')
        serializer = BookInfoSerializer(data , many=True)
        return Response({'ok': True, 'data': serializer.data} , status=200)
    
    def post(self , request , format=None):
        serializer = BookInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data}, status=200)
        
        return Response({'ok': False , 'message': 'something went wrong!'})
    
    def patch(self , request , format=None):
        req_data = request.data 

        object_instance = BookInfo.objects.get(id=req_data['id'])
        print(object_instance)

        serializer = BookInfoSerializer(object_instance , data=req_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True, 'data': serializer.data}, status=200)
        
        return Response({'ok': False, 'message': serializer.errors}, status=400)
    
    def delete(self, request , format=None):
        object_instance = BookInfo.objects.get(id=request.data['id'])
        object_instance.delete()

        return Response(" Deleted Successfully!")