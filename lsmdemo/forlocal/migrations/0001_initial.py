# Generated by Django 3.2.8 on 2021-12-19 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='aloki1.PNG', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('realme', 'realme'), ('redmi', 'redmi'), ('samsung', 'samsung'), ('apple', 'apple'), ('one plus', 'one plus'), ('motorola', 'motorola'), ('nokia', 'nokia'), ('honor', 'hobor'), ('asus', 'asus'), ('poco', 'poco')], max_length=100, null=True)),
                ('model', models.CharField(max_length=100, null=True)),
                ('color', models.CharField(max_length=100, null=True)),
                ('ram', models.CharField(choices=[('1GB', '1GB'), ('2GB', '2GB'), ('4GB', '4GB'), ('6GB', '6GB'), ('8GB', '8GB')], max_length=100, null=True)),
                ('rom', models.CharField(choices=[('2GB', '2GB'), ('32GB', '32GB'), ('64GB', '64GB'), ('128GB', '12GB'), ('256GB', '256GB')], max_length=100, null=True)),
                ('price', models.FloatField(max_length=10, null=True)),
                ('offer', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('available', 'available'), ('not available', 'not available')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=100, null=True)),
                ('contact_email', models.CharField(max_length=100, null=True)),
                ('contact_num', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('district', models.CharField(max_length=100, null=True)),
                ('timming', models.CharField(max_length=100, null=True)),
                ('rating', models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], max_length=10, null=True)),
                ('pay_mode', models.CharField(choices=[('PAYTM', 'PAYTM'), ('CASH', 'CASH'), ('GPAY', 'GPAY'), ('PHONEPE', 'PHONEPE')], max_length=100, null=True)),
                ('established', models.CharField(max_length=10, null=True)),
                ('verificatoin', models.CharField(choices=[('VERIFIED', 'VERIFIED'), ('NON VERIFIED', 'NON VERIFIED')], max_length=100, null=True)),
                ('discount', models.CharField(max_length=100, null=True)),
                ('offer', models.CharField(max_length=100, null=True)),
                ('shop_pic', models.ImageField(blank=True, default='aloki1.PNG', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('description', models.TextField(max_length=100, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='forlocal.owner')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='forlocal.smartphone')),
            ],
        ),
    ]
