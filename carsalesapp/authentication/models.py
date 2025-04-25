from django.contrib.auth.models import User
from django.db import models

# ────────────────────────────────────────────────────────────────────────────────────────────────
# User Profile Model
# ────────────────────────────────────────────────────────────────────────────────────────────────
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    is_external = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'


