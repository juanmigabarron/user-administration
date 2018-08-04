from django.contrib import admin

from user_administration.admin import admin_site

from .models import User


@admin.register(User, site=admin_site)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'iban')

    def has_change_permission(self, request, obj=None):
        permission = False
        if obj and request.user == obj.created_by:
            permission = True
        return permission

    def has_delete_permission(self, request, obj=None):
        permission = False
        if obj and request.user == obj.created_by:
            permission = True
        return permission
