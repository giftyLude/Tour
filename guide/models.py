from email.policy import default
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Region(models.Model):
    name = models.CharField(default="", max_length=80)
    slug = models.SlugField(default="Will-be-added")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Region, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("region-detail", kwargs={"slug": self.slug})


class Site(models.Model):
    name = models.CharField(default="", max_length=250)
    image = models.FileField(upload_to="site_images", null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    town = models.CharField(default="", max_length=250)
    bio = RichTextUploadingField()
    gpsAddress = models.CharField(default="", max_length=50)
    gmapLocation = models.CharField(default="", max_length=250)
    rating = models.IntegerField(default=1, max_length=5)
    users = models.ManyToManyField(User, blank=True)
    slug = models.SlugField(default="will-be-added")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-rating"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Site, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("site-detail", kwargs={"pk": self.pk})

    def count_rating(self):
        return range(self.rating)


class Lodge(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to="lodge_images", null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    town = models.CharField(default="", max_length=250)
    bio = RichTextUploadingField()
    gmapLocation = models.CharField(default="", max_length=250)
    rating = models.IntegerField(default=1, max_length=5)
    users = models.ManyToManyField(User, blank=True)
    slug = models.SlugField(default="will-be-added")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-rating"]

    def save(self):
        self.slug = slugify(self.name)
        return super(Lodge, self).save()

    def get_absolute_url(self):
        return reverse("lodge-detail", kwargs={"pk": self.pk})

    def count_rating(self):
        return range(self.rating)


class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to="event_images", null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    town = models.CharField(default="", max_length=250)
    desc = RichTextUploadingField(default="")
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    users = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date"]

    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"pk": self.pk})
