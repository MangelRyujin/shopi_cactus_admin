# Generated by Django 4.2.2 on 2023-07-10 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_remove_order_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
    ]
