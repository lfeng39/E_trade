# Generated by Django 3.2.10 on 2023-10-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAL', '0003_listing_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='status',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]