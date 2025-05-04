from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import TestDriveRecord, ServiceRecord
from .utils import msg_service_status, msg_booking_status, notify_staff_if_needed
from django.db.models.signals import pre_save


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Signal for Test Drive pre save status
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
@receiver(pre_save, sender=TestDriveRecord)
def capture_previous_booking_status(sender, instance, **kwargs):
    if instance.pk:
        old = TestDriveRecord.objects.get(pk=instance.pk)
        instance._old_status = old.status


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Signal for Service pre save status
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
@receiver(pre_save, sender=ServiceRecord)
def capture_previous_booking_status(sender, instance, **kwargs):
    if instance.pk:
        old = ServiceRecord.objects.get(pk=instance.pk)
        instance._old_status = old.status

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Signal for Test Drive notifications on status change
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
@receiver(post_save, sender=TestDriveRecord)
def notify_user_test_drive_status(sender, instance, created, **kwargs):
    if not created and hasattr(instance, '_old_status') and instance._old_status != instance.status:
        msg_booking_status(instance)
        notify_staff_if_needed(instance)

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Signal for Service notifications on status change
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
@receiver(post_save, sender=ServiceRecord)
def notify_user_service_status(sender, instance, created, **kwargs):
    if not created and hasattr(instance, '_old_status') and instance._old_status != instance.status:
        msg_booking_status(instance)
        notify_staff_if_needed(instance)