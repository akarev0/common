# Register your models here.
from django.contrib import admin

from .models import Tenant, Room, Journal, Key


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'phone')
    search_fields = ('first_name', 'last_name', 'phone', 'date_of_birth')
    list_filter = ('date_of_birth', 'last_name')


class JournalAdmin(admin.ModelAdmin):
    list_display = ('key_out_date', 'key_in_date', 'tenant_id', 'key_id')
    list_display_links = ('tenant_id', 'key_id')
    search_fields = ('tenant_id', 'key_id')


admin.site.register(Journal, JournalAdmin)
admin.site.register(Room)
admin.site.register(Key)



