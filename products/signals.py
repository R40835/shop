import time # might need to sleep when we have to many emails per seconds

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core import mail
from django.core.mail import EmailMessage
from django.conf import settings

from .models import Product, Followers


@receiver(post_save, sender=Product)
def calling_user(sender, instance, created, **kwargs):
    """
    Firing signal upon user call and sending relevant 
    data to client through consumer.
    """
    if created:
        followers = Followers.objects.all()
        if followers.exists():
            connection = mail.get_connection()
            connection.open()
            for follower in followers:
                email = EmailMessage(
                    'New Content!',
                    'Dear Customer\n\nWe\'ve got brand new products that may be of interest to you. Check it out! 127.0.0.1:8000', 
                    settings.EMAIL_HOST_USER,
                    [f'{follower.email}'],
                    connection=connection,
                )
                connection.send_messages([email])
            connection.close()
