# Generated by Django 4.2.2 on 2023-07-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.PositiveIntegerField(default=0, verbose_name='Id de usuario'),
            preserve_default=False,
        ),
    ]
