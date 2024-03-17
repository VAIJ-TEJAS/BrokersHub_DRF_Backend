from django.db import models
from user.models import User


class Advertisement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    contact = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    transaction_type = models.CharField(max_length=50)

    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    downpayment = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True
    )
    ratio_x = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ratio_y = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    monthly_rent = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True
    )

    image = models.ImageField(upload_to="advertisement_images/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.transaction_type}"
