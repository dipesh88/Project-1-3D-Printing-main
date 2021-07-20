from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# table for all parts
class Part(models.Model):
    part = models.FileField(upload_to="uploaded_parts")

# table for user data
class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parts = models.ManyToManyField(Part, blank=True)

@receiver(post_save, sender=User)
def update_consumer(sender, instance, created, **kwargs):
    if created:
        Consumer.objects.create(user=instance)
    else:
        instance.consumer.save()
