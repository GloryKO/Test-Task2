from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def get_task_list(request):
    task = Task.objects.all()
    serializer =TaskSerializer(task,Many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_single_task_details(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task,Many=False)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.data.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    


