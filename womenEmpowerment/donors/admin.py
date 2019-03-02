from django.contrib import admin
from .models import Donor, Transaction
# Register your models here.

class DonorAdmin(admin.ModelAdmin):
    list_display = ('donor_id', 'total_amount')
    
    def get_ordering(self, request):
        return ['id']

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction_sender', 'transaction_receiver', 'amount')

    def get_ordering(self, request):
        return ['id']

admin.site.register(Donor, DonorAdmin)
admin.site.register(Transaction, TransactionAdmin)