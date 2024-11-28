from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BorrowedBooksSerializer , GetBookSerializer
from .models import BorrowedBooks
# Create your views here.

class BorrowedBooksView(APIView):
    def get(self , request , format=None):
        data = BorrowedBooks.objects.all().order_by('-id')
        serializer = GetBookSerializer(data , many=True)
        return Response({'ok': True, 'data': serializer.data} , status=200)
    
    def post(self , request , format=None):
        serializer = BorrowedBooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data}, status=200)
        
        return Response({'ok': False , 'message': serializer.errors})
    
    def patch(self , request , format=None):
        req_data = request.data

        object_instance = BorrowedBooks.objects.get(id=req_data['id'])
        print(object_instance)

        serializer = BorrowedBooksSerializer(object_instance , data=req_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True, 'data': serializer.data}, status=200)
        
        return Response({'ok': False, 'message': 'something went wrong'})
    
    def delete(self, request , format=None):
        req_data = request.data

        object_instance = BorrowedBooks.objects.get(id=req_data['id'])
        object_instance.delete()

        return Response(" Deleted Successfully!")