from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Organization(models.Model):
    main_logo = models.ImageField(upload_to='organizations/logos/%Y/%m/%d')
    organization_name = models.CharField(max_length=100)
    about_organization = models.TextField()
    project_name = models.CharField(max_length=100)
    project_description = models.TextField() 
    required_funding = models.IntegerField()
    total_amount = models.CharField(max_length=25)
    impact = models.TextField()
    deadline = models.DateTimeField(auto_now_add=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    resources_providing = models.TextField(blank=True)
    
    def get_percentage(self):
        return (self.total_amount//self.required_funding)*100