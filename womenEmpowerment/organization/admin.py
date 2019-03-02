from django.contrib import admin
from .models import Organization
# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization_name', 'deadline')
    list_display_links = ('id', 'organization_name')
    search_fields = ('organization_name',)
    list_per_page = 25 

    def get_ordering(self, request):
        return ['id']

admin.site.register(Organization, OrganizationAdmin)