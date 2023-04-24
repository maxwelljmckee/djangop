from rest_framework import serializers
from .models import Status, Task

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['name', 'id']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'statusId', 'id']