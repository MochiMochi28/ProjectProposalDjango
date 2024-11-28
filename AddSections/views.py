from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AddSectionsSerializer
from rest_framework.parsers import JSONParser
from .models import AddSections
# Create your views here.

class AddSectionsView(APIView):
    
    def get(self , request , format=None):
        data = AddSections.objects.all().order_by('-id')
        serializer = AddSectionsSerializer(data , many=True)
        return Response({'ok': True, 'data': serializer.data} , status=200)
    
    def post(self , request , format=None):
        data = JSONParser().parse(request)

        serializer = AddSectionsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data}, status=200)
        
        return Response({'ok': False , 'message': 'something went wrong!'})
    
    def patch(self , request , format=None):
        req_data = JSONParser().parse(request)

        object_instance = AddSections.objects.get(id=req_data['id'])
        print(object_instance)

        serializer = AddSectionsSerializer(object_instance , data=req_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True, 'data': serializer.data}, status=200)
        
        return Response({'ok': False, 'message': 'something went wrong'})
    
    def delete(self, request , format=None):
        req_data = JSONParser().parse(request)

        object_instance = AddSections.objects.get(id=req_data['id'])
        object_instance.delete()

        return Response(" Deleted Successfully!")