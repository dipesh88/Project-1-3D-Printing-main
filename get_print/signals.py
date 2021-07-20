from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Consumer


@receiver(post_save, sender=User)
def update_consumer(sender, instance, created, **kwargs):
    if created:
        Consumer.objects.create(user=instance)
    else:
        instance.consumer.save()
