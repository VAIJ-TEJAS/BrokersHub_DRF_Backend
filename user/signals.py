from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from advertisement.models import Advertisement
from requirement.models import Requirement
from .models import User

from brokershub.celery import app

@app.task
def send_notification_email(instance_id, model_name):
    # Determine the model class based on model_name
    if model_name == "Requirement":
        model_class = Requirement
    elif model_name == "Advertisement":
        model_class = Advertisement
    else:
        raise ValueError(f"Unsupported model_name: {model_name}")

    # Fetch the instance from the database
    instance = model_class.objects.get(id=instance_id)
    
    subject = f'New {model_name} Posted'
    message = f"A new {model_name.lower()} titled '{instance.title}' has been posted in {instance.city}, {instance.state}. Check it out!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email for user in User.objects.filter(state=instance.state, city=instance.city, email__isnull=False) if user.email]
    
    # Send an individual email to each recipient
    for recipient in recipient_list:
        send_mail(subject, message, from_email, [recipient], fail_silently=False)

@receiver(post_save, sender=Advertisement)
def advertisement_post_save(sender, instance, created, **kwargs):
    if created:
        send_notification_email.delay(instance.id, "Advertisement")

@receiver(post_save, sender=Requirement)
def requirement_post_save(sender, instance, created, **kwargs):
    if created:
        send_notification_email.delay(instance.id, "Requirement")
