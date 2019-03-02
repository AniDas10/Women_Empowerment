from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class WomanNeedsSupport(models.Model):
    main_photo = models.ImageField(upload_to='women/photos/%Y/%m/%d')
    about_me = models.TextField()
    project_name = models.CharField(max_length=100)
    project_description = models.TextField() 
    requirements = models.TextField()
    deadline = models.DateTimeField(auto_now_add=True)
    percentage_funded = models.IntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

class WomanNeedsJob(models.Model):
    main_photo = models.ImageField(upload_to='women/photos/%Y/%m/%d')
    about_me = models.TextField()
    skills = models.TextField()
    linkedIn = models.CharField(max_length=250)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)