# Generated by Django 4.1 on 2022-08-23 14:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("fscohort", "0002_alter_student_options_student_about_student_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="country",
            field=models.CharField(
                choices=[
                    ("TR", "Turkey"),
                    ("US", "America"),
                    ("DE", "Germany"),
                    ("FR", "France"),
                ],
                default="TR",
                max_length=2,
                verbose_name="Ülke",
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="registered_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="updated_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
