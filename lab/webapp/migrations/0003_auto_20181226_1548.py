# Generated by Django 2.1 on 2018-12-26 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20181220_1452'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('deliver_order', 'Взять заказ')]},
        ),
    ]
