# Generated by Django 3.2.8 on 2021-12-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forlocal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='name',
            new_name='owner_name',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='product',
        ),
        migrations.AddField(
            model_name='smartphone',
            name='shop',
            field=models.ManyToManyField(to='forlocal.Shop'),
        ),
    ]