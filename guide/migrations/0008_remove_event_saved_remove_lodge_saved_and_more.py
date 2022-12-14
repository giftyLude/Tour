# Generated by Django 4.1 on 2022-09-12 10:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("guide", "0007_event_saved_lodge_saved_site_saved"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="saved",
        ),
        migrations.RemoveField(
            model_name="lodge",
            name="saved",
        ),
        migrations.RemoveField(
            model_name="site",
            name="saved",
        ),
        migrations.AddField(
            model_name="event",
            name="users",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="lodge",
            name="users",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="site",
            name="users",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
