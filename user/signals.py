from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
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
    text_content = f"A new {model_name.lower()} titled '{instance.title}' has been posted in {instance.city}, {instance.state}. Check it out!"
    html_content = f"""\
    <html>
      <head></head>
      <body>
        <p>Hi there,<br>
           A new {model_name.lower()} titled "<b>{instance.title}</b>" has been posted in {instance.city}, {instance.state}.<br>
           Check it out by clicking the button below!
        </p>
        <p><a href="YOUR_REDIRECT_LINK_HERE" style="background-color: #0045ff; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block;">View {model_name}</a></p>
      </body>
    </html>
    """
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email for user in User.objects.filter(state=instance.state, city=instance.city, email__isnull=False) if user.email]

    # Send an individual email to each recipient with HTML content
    for recipient in recipient_list:
        msg = EmailMultiAlternatives(subject, text_content, from_email, [recipient])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

@receiver(post_save, sender=Advertisement)
def advertisement_post_save(sender, instance, created, **kwargs):
    if created:
        send_notification_email.delay(instance.id, "Advertisement")

@receiver(post_save, sender=Requirement)
def requirement_post_save(sender, instance, created, **kwargs):
    if created:
        send_notification_email.delay(instance.id, "Requirement")
