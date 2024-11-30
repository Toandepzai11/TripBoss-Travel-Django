from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from django.contrib.auth.models import User  # Import User model

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Temporarily make it nullable

    def __str__(self):
        return self.title
    def short_content(self):
        # Return only the first 50 characters of the content
        return self.body[:202] + '...' if len(self.body) > 50 else self.body

# delete image whenever user delete the post
@receiver(post_delete, sender=Post)
def delete_image_on_post_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)