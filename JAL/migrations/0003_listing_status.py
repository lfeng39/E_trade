# Generated by Django 3.2.10 on 2023-10-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAL', '0002_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='status',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
