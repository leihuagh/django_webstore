# Generated by Django 2.0 on 2018-07-18 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_auto_20180701_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='price',
            new_name='cost',
        ),
    ]
