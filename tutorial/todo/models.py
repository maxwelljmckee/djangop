from django.db import models

# Create your models here.
class Status(models.Model):
    name: models.CharField(max_length=64)

class Task(models.Model):
    title: models.CharField(max_length=250)
    description: models.TextField()
    status: models.ForeignKey(Status, on_delete=models.CASCADE)