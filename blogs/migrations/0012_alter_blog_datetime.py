# Generated by Django 3.2.12 on 2023-03-06 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_alter_blog_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 3, 6, 19, 4, 37, 489063)),
        ),
    ]
