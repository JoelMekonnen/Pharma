from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    Bio = models.TextField(blank=True, null=True)
    Profile_Image = models.ImageField(null=True)
    Birth_Date = models.DateField(blank=True, null=True)
    Address = models.CharField(default=None, max_length=255, blank=True, null=True)

    def __str__(self):
        return User.objects.get(pk=self.user_id).get_username()
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


