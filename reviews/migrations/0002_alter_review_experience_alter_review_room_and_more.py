# Generated by Django 5.1.1 on 2024-09-26 06:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "experiences",
            "0002_alter_experience_category_alter_experience_host_and_more",
        ),
        ("reviews", "0001_initial"),
        ("rooms", "0003_alter_amenity_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="experience",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="experiences.experience",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="rooms.room",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
