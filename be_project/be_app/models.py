from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# email = models.EmailField(max_length=100, unique=True)
	image = models.ImageField(blank=True, null=True)
	# username = models.CharField(max_length=50)


	def __str__(self):
		# return "%s: %s" % (self.id, self.user)
		return self.user.username

"""Automatically Create A User Profile When A New User IS Registered"""
@receiver(post_save, sender=User)
def profile_creation(sender, instance, created, *args, **kwargs):
	if created:
		profile = Profile(user=instance)
		profile.save()


# User = get_user_model()


class Post(models.Model):
	title = models.CharField(max_length=20)
	description = models.CharField(max_length=180)
	image = models.ImageField(blank=True, null=True)


	"""should I keep Profile or put User?"""
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class PostImage(models.Model):
	post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/')

	def __str_(self):
		return self.post.title




