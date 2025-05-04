from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# ────────────────────────────────────────────────────────────────────────────────────────────────
#
# ────────────────────────────────────────────────────────────────────────────────────────────────
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # New User created => Create corresponding Profile
        Profile.objects.create(user=instance)
    # else:
        # Existing User updated => Save Profile just in case
        # instance.profile.save()