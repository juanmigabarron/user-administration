from user_administration.admin import admin_site
from django.contrib.auth.admin import UserAdmin

from .models import User, BankAccount

admin_site.register(User, UserAdmin)
admin_site.register(BankAccount)
