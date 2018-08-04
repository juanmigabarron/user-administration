from django.conf import settings
from django.db import models

from .validators import validate_iban


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    iban = models.CharField(max_length=34, validators=[validate_iban])
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
