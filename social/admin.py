from django.contrib import admin
from . import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership_status']
    list_editable = ['membership_status']
    ordering = ['user__first_name', 'user__last_name']
    list_select_related = ['user']
    list_per_page = 10
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
