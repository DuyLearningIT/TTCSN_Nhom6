from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.

class User(models.Model):
    fullName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=255)
    userType = models.CharField(max_length=50, default="Silver User", blank=True)
    loyaltyPoints = models.IntegerField(default=0, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

