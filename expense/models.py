from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Register(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Mobile = models.CharField(max_length=10)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    Date = models.DateField()
    Salary = models.IntegerField()
    Other_Income = models.IntegerField()
    Food = models.IntegerField()
    Transport = models.IntegerField()
    Apparel = models.IntegerField()
    Education = models.IntegerField()
    Grocery = models.IntegerField()
    Health = models.IntegerField()
    Other_Expense = models.IntegerField()
