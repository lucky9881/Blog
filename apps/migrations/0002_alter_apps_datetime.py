# Generated by Django 3.2.12 on 2023-03-06 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apps',
            name='datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 3, 6, 17, 56, 50, 819217)),
        ),
    ]
