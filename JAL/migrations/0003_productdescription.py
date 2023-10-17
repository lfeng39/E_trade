# Generated by Django 3.2.22 on 2023-10-16 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAL', '0002_delete_productdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(blank=True, max_length=20)),
                ('bullet_point_01', models.CharField(blank=True, max_length=500)),
                ('bullet_point_02', models.CharField(blank=True, max_length=500)),
                ('bullet_point_03', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]