from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=65, unique=True)
    country = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=65)
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name="cars",
        on_delete=models.SET_NULL, null=True
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self) -> str:
        return f"{self.manufacturer}: {self.model}"
