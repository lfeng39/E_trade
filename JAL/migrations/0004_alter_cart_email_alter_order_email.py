# Generated by Django 4.2.6 on 2024-01-12 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAL', '0003_alter_useraccount_email_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='email',
            field=models.EmailField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=80),
        ),
    ]