from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=256)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=256)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)

class Feedback(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    feedback = models.TextField()
    time = models.DateTimeField(auto_now_add=True)    
