# Generated by Django 4.2 on 2023-10-31 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAL', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdescription',
            name='url',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
