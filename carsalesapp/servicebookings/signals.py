from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import TestDriveRecord, ServiceRecord
from .utils import send_test_drive_status_email, send_service_status_email


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Signal for test drive notifications on status change
# ────────────────────────────────────────────────────────────────────────────────────────────────
@receiver(post_save, sender=TestDriveRecord)
def notify_user_test_drive_status(sender, instance, created, **kwargs):
    if not created:  
        send_test_drive_status_email(instance)


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Signal for test drive notifications on status change
# ────────────────────────────────────────────────────────────────────────────────────────────────
@receiver(post_save, sender=ServiceRecord)
def notify_user_service_status(sender, instance, created, **kwargs):
    if not created:  
        send_service_status_email(instance)