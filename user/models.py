from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    my_referral_code = models.CharField(max_length=255, unique=True, blank=True)
    other_referral_code = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    send_email = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        if not self.my_referral_code:
            # Generating referral code after the user has an ID
            self.my_referral_code = self.generate_referral_code()
            self.save()

    def generate_referral_code(self):
        # Ensure first_name and last_name are not empty
        first_name_part = self.first_name[:3].upper() if self.first_name else "USR"
        last_name_part = self.last_name[-3:].upper() if self.last_name else "USR"
        return f"{first_name_part}{last_name_part}{self.id}"

    def __str__(self):
        return self.username
