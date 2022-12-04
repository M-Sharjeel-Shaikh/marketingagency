from django.db import models

# Create your models here.
class Clients(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    Email=models.CharField(max_length=30)
    Text_area=models.TextField(max_length=1500, blank=False)
    
    