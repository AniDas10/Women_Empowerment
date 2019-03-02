from django.contrib import admin
from .models import WomanNeedsSupport, WomanNeedsJob
# Register your models here.
class WomanNeedsSupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'percentage_funded', 'deadline')
    list_display_links = ('id',)
    # search_fields = ('name',)
    list_per_page = 25 

    def get_ordering(self, request):
        return ['id']

class WomanNeedsJobAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 25 

    def get_ordering(self, request):
        return ['id']

admin.site.register(WomanNeedsJob, WomanNeedsJobAdmin)

admin.site.register(WomanNeedsSupport, WomanNeedsSupportAdmin)