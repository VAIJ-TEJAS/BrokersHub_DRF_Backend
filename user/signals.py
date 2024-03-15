from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from advertisement.models import Advertisement
from requirement.models import Requirement
from .models import User

def send_notification_email(instance, model_name):
    subject = f'New {model_name} Posted'
    message = f"A new {model_name.lower()} titled '{instance.title}' has been posted in {instance.city}, {instance.state}. Check it out!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email for user in User.objects.filter(state=instance.state, city=instance.city, email__isnull=False) if user.email]
    
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

@receiver(post_save, sender=Advertisement)
def advertisement_post_save(sender, instance, created, **kwargs):
    if created:
        send_notification_email(instance, "Advertisement")

@receiver(post_save, sender=Requirement)
def requirement_post_save(sender, instance, created, **kwargs):
    if created:
        send_notification_email(instance, "Requirement")
