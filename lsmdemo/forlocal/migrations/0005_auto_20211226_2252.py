# Generated by Django 3.2.8 on 2021-12-26 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forlocal', '0004_alter_smartphone_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='shop',
        ),
        migrations.AddField(
            model_name='smartphone',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='forlocal.shop'),
        ),
    ]
