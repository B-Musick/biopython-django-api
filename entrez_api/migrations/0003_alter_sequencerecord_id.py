# Generated by Django 5.0.6 on 2024-06-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrez_api', '0002_sequencerecord_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequencerecord',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]