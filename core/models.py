from django.db import models
from PIL import Image
from django.utils.timezone import now
from apps.user.models import User

class CoreUserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

