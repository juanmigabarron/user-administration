from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    created_by = models.ForeignKey('administration.User', on_delete=models.CASCADE, blank=True, null=True)


class BankAccount(models.Model):
    iban = models.CharField(max_length=34)
    user = models.ForeignKey('administration.User', on_delete=models.CASCADE)
