from django.http import HttpResponse
from django.shortcuts import render
from .models import Status, Task
from rest_framework import viewsets
from .serializers import StatusSerializer, TaskSerializer

# Create your views here.
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
