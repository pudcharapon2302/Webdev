from django.db import models

# Create your models here.
class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=200)
    dob = models.DateField()
    email = models.EmailField()