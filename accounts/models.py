from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    address = models.TextField("Delivery address", null=True, blank=True)

    def __str__(self):
        return self.username
