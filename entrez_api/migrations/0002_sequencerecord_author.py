# Generated by Django 5.0.6 on 2024-06-05 16:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrez_api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='sequencerecord',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sequence_records', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
