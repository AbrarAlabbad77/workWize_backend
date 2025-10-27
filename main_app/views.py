from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ManagerSerializer
from .models import Manager, Task, TeamMember, Project


# Create your views here.
class ManagerIndex(APIView):
    
    def get(self,request):
        querset = Manager.objects.all()
        serializer = ManagerSerializer(querset, many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        try:
            serializer = ManagerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.error, status=status.HTTP_400_bad_request)
        except Exception as error:
            return Response({'ERROR':str(error)}, status==status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
class ManagerDetails(APIView):
    
    #  get specific manager by id 
    def get(self, request, manager_id):
        queryset = Manager.objects.get(id=manager_id)
        serializer = ManagerSerializer(queryset)
        return Response(serializer.data)
    
    
    # Update manager info
    def put(self,request, manager_id):
        try:
            querset = get_object_or_404(Manager, id=manager_id)
            serializer = ManagerSerializer(querset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_bad_request)
        except Exception as error:
            return Response({'ERROR':str(error)}, status==status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # delete manager 
    def delete(self, request, manager_id):
        try:
            querset = get_object_or_404(Manager, id=manager_id)
            querset.delete()
            return Response({'message:' f' Mnanget {manager_id} has been deleted'},status=status_204)
        except Exception as error:
            return Response({'ERROR': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
    










        