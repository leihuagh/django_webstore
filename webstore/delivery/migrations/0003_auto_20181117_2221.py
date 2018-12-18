# Generated by Django 2.1.3 on 2018-11-17 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_delivery_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliverypricing',
            old_name='cost_per_kg',
            new_name='cost',
        ),
        migrations.AddField(
            model_name='deliverypricing',
            name='max_weight',
            field=models.FloatField(default=30.0),
        ),
    ]