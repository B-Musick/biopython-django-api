# Generated by Django 5.0.6 on 2024-06-05 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrez_api', '0003_alter_sequencerecord_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequencerecord',
            name='id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]