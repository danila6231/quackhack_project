# Generated by Django 5.1.5 on 2025-01-19 07:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0004_session_prompt_guess"),
    ]

    operations = [
        migrations.AddField(
            model_name="session",
            name="image_url",
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
