from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import serializers

# Nuetras Importaciones
from .models import Tarea
from .serializers import TareaSerializer


@api_view(['GET'])
def getTarea(request):
    tarea = Tarea.objects.all()
    serializer = TareaSerializer(tarea, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postTarea(request):
    data = request.data
    tarea = Tarea.objects.create(
        body=data['body']
    )
    serializer = TareaSerializer(tarea, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def putTarea(request, pk):
    data = request.data
    tarea = Tarea.objects.get(id=pk)
    serializer = TareaSerializer(instance=tarea, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTarea(request, pk):
    # data = request.data
    tarea = Tarea.objects.get(id=pk)
    tarea.delete()
    return Response('Blog post deleted')
