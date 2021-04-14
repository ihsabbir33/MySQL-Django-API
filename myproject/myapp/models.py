from django.db import models
import time

class Registration(models.Model):
    username = models.CharField(max_length=70)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)

