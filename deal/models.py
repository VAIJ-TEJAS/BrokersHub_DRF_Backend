from django.db import models
from advertisement.models import Advertisement
from requirement.models import Requirement
from user.models import User


class Deal(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
        ("COMPLETED", "Completed"),
    ]

    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE, blank=True, null=True)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, blank=True, null=True)
    deal_maker = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")

    def __str__(self):
        return f"Deal {self.id} - {self.status}"
