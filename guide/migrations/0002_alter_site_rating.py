# Generated by Django 4.1 on 2022-08-31 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guide", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="rating",
            field=models.IntegerField(default=1, max_length=5),
        ),
    ]
