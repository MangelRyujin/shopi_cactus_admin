# Generated by Django 4.2.2 on 2023-07-10 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0005_alter_order_cost_alter_order_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cost',
        ),
    ]
