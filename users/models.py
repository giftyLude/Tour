from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from guide.models import Site, Lodge, Event


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=100)
    email = models.EmailField()
    GENDER_OPTIONS = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    gender = models.CharField(choices=GENDER_OPTIONS, default="Male", max_length=10)
    sites = models.ManyToManyField(Site, blank=True)
    lodges = models.ManyToManyField(Lodge, blank=True)
    events = models.ManyToManyField(Event, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="")

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
