from django.contrib import admin

from user_administration.admin import admin_site

from .models import BankAccount, User


@admin.register(User, site=admin_site)
class UserModelAdmin(admin.ModelAdmin):
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

@admin.register(BankAccount, site=admin_site)
class BankAccountModelAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        permission = False
        if obj and request.user == obj.user.created_by:
            permission = True
        return permission
    
    def has_delete_permission(self, request, obj=None):
        permission = False
        if obj and request.user == obj.user.created_by:
            permission = True
        return permission
