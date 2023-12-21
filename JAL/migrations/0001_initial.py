# Generated by Django 4.2.6 on 2023-12-21 06:42

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
                ('user_id', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('product', models.CharField(blank=True, max_length=3000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(blank=True, max_length=1000)),
                ('sku', models.CharField(blank=True, max_length=1000)),
                ('title', models.CharField(blank=True, max_length=20)),
                ('coupon_code', models.CharField(blank=True, max_length=20)),
                ('coupon_type', models.CharField(blank=True, max_length=20)),
                ('type_cash', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type_percentage', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('status', models.CharField(blank=True, max_length=2)),
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
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(blank=True, max_length=20)),
                ('sku', models.CharField(blank=True, max_length=30)),
                ('sku_sn', models.CharField(blank=True, max_length=50)),
                ('title', models.CharField(blank=True, max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bullet_point', models.TextField(blank=True, max_length=3000)),
                ('description', models.TextField(blank=True, max_length=3000)),
                ('first_img', models.CharField(blank=True, max_length=300)),
                ('status', models.CharField(blank=True, max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=20)),
                ('user_id', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('product', models.CharField(blank=True, max_length=3000)),
                ('user_shipping', models.CharField(blank=True, max_length=3000)),
                ('status', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
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
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bullet_point', models.CharField(blank=True, max_length=3000)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('first_img', models.CharField(blank=True, max_length=300)),
                ('status', models.CharField(blank=True, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Promote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=20)),
                ('code', models.CharField(blank=True, max_length=20)),
                ('img', models.CharField(blank=True, max_length=500)),
                ('bullet_point_01', models.CharField(blank=True, max_length=500)),
                ('bullet_point_02', models.CharField(blank=True, max_length=500)),
                ('bullet_point_03', models.CharField(blank=True, max_length=500)),
                ('url', models.CharField(blank=True, max_length=500)),
                ('channel', models.CharField(blank=True, max_length=500)),
                ('status', models.CharField(blank=True, max_length=2)),
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
                ('email', models.EmailField(blank=True, max_length=30)),
                ('password', models.CharField(blank=True, max_length=20)),
                ('email_platform', models.EmailField(blank=True, max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('street', models.CharField(blank=True, max_length=300)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('code', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(blank=True, max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
