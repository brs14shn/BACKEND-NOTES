# Generated by Django 4.1 on 2022-09-01 18:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="UsersProfile", new_name="UserProfile",),
    ]
