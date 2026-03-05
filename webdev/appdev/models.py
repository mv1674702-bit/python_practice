from django.db import models

# Create your models here.

class Tableone(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    
    file=models.FileField(upload_to='media/', null=True, blank=True)