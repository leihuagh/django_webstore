# Generated by Django 2.0 on 2018-07-18 21:07

from django.db import migrations
import webstore.cash.fields


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20180218_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='value',
            field=webstore.cash.fields.CashField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
