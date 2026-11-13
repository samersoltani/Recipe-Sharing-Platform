from django.db import models
from django.contrib.auth.models import User
from PIL import Image 
from pathlib import Path




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.jpg', upload_to='profile_avatars')


    def __str__(self):
        return self.user.username




def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    if not self.avatar:
        return

    image_path = Path(self.avatar.path)

    if not image_path.is_file():
        return

    with Image.open(image_path) as img:
        if img.height > 300 or img.width > 300:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(image_path)