from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(blank=True, null=True)


	def __str__(self):
		# return "%s: %s" % (self.id, self.user)
		return self.user.username


@receiver(post_save, sender=User)
def profile_creation(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)