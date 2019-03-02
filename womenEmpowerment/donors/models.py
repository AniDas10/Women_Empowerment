from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Donor(models.Model):
	donor=models.OneToOneField(User,on_delete="models.CASCADE")
	Amount=models.IntegerField()


class Transaction(models.Model):
	donor_id=models.ForeignKey(User,on_delete="models.CASCADE")
	receiver_id=models.ForeignKey(User,on_delete="models.CASCADE")
	amount=models.IntegerField()
	time=models.DateTimeField(auto_add_now=True)

