from django.db import models

class User(models.Model):
    username = models.CharField(max_length=15)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=15)
    address = models.CharField(max_length=100)