from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Devices(models.Model):
    device_choices = [("LAPTOP", "laptop"), ("MOBILE", "mobile"), ("TABLET", "tablet")]
    category = models.CharField(max_length=50, choices=device_choices, default="MOBILE")
    name = models.CharField(max_length=100, blank=False, null=False)
    model = models.CharField(max_length=100, blank=False, null=False)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    ram = models.CharField(max_length=100, blank=False, null=False)
    internal_storage = models.CharField(max_length=100, blank=False, null=False)
    battery = models.CharField(max_length=100, blank=False, null=False)
    camera = models.CharField(max_length=100, blank=False, null=False)
    processor = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DeviceSold(models.Model):
    device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sold_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.device.name + "sold to" + self.user.username