# Generated by Django 3.2.8 on 2021-12-29 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forlocal', '0008_alter_smartphone_shop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smartphone',
            old_name='shop',
            new_name='owner',
        ),
    ]