# Generated by Django 3.2.10 on 2022-12-05 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsinInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(blank=True, max_length=20)),
                ('sku', models.CharField(blank=True, max_length=30)),
                ('sku_sn', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('asin', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(blank=True, max_length=20)),
                ('listing_7', models.CharField(blank=True, max_length=140)),
                ('A_970', models.CharField(blank=True, max_length=140)),
                ('A_300', models.CharField(blank=True, max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20)),
                ('user_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(blank=True, max_length=20)),
                ('bullet_point_00', models.CharField(blank=True, max_length=500)),
                ('bullet_point_01', models.CharField(blank=True, max_length=500)),
                ('bullet_point_02', models.CharField(blank=True, max_length=500)),
                ('bullet_point_03', models.CharField(blank=True, max_length=500)),
                ('bullet_point_04', models.CharField(blank=True, max_length=500)),
                ('bullet_point_05', models.CharField(blank=True, max_length=500)),
                ('bullet_point_06', models.CharField(blank=True, max_length=500)),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(blank=True, max_length=20)),
                ('sku', models.CharField(blank=True, max_length=30)),
                ('sku_sn', models.CharField(blank=True, max_length=50)),
                ('title', models.CharField(blank=True, max_length=300)),
                ('price', models.IntegerField()),
                ('bullet_point', models.CharField(blank=True, max_length=3000)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('first_img', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SalesStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(blank=True, max_length=20)),
                ('new', models.IntegerField()),
                ('onSale', models.IntegerField()),
                ('unavailabe', models.IntegerField()),
                ('restock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=20)),
                ('user_name', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('street', models.CharField(blank=True, max_length=300)),
                ('ctiy', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('code', models.CharField(blank=True, max_length=5)),
            ],
        ),
    ]
