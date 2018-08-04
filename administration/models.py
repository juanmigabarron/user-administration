from django.conf import settings
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class BankAccount(models.Model):
    iban = models.CharField(max_length=34)
    user = models.ForeignKey('administration.User', on_delete=models.CASCADE)
