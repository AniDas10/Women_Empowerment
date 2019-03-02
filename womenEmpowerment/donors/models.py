from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Donor(models.Model):
	donor=models.OneToOneField(User,on_delete="models.CASCADE")
	total_amount = models.CharField(max_length=20, null=True)


class Transaction(models.Model):
	transaction_sender = models.CharField(max_length=256)
	transaction_receiver = models.ForeignKey(User, on_delete=models.CASCADE)
	amount = models.IntegerField()
	time = models.DateTimeField(auto_now_add=True)

