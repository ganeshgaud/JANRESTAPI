from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=64)
    eaddr=models.CharField(max_length=64)
    esal=models.IntegerField()
    eno=models.IntegerField()
