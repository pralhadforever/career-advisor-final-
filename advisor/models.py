from django.db import models

# Create your models here.
class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=10)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    userId = models.AutoField(primary_key=True)

class Contact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=10)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    userMessage = models.CharField(max_length=1000)

def __str__(self):
    return(f"{self.firstName}{self.lastName}")