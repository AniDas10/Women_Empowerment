from django.contrib import admin
from .models import WomanNeedsSupport, WomanNeedsJob
# Register your models here.
class WomanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'percentage_funded', 'deadline')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25 

    def get_ordering(self, request):
        return ['id']

admin.site.register(Woman, WomanAdmin)