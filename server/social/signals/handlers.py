from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from social.models import Customer


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_profile_after_creating_new_user(sender, **kwargs):
    if kwargs['created']:
        Customer.objects.create(user=kwargs['instance'])
