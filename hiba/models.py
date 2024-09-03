from django.db import models

# Create your models here.
class table1(models.Model):
    Name=models.CharField(max_length=(50))
    Number=models.IntegerField(20)