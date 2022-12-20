# Generated by Django 4.1.4 on 2022-12-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("number", models.IntegerField(default=1)),
                ("about", models.TextField(blank=True, null=True)),
                ("register_date", models.DateTimeField(auto_now_add=True)),
                ("last_update_date", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"verbose_name_plural": "student_list", "ordering": ["number"],},
        ),
    ]
