# Generated by Django 3.2.12 on 2023-02-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
                ('email', models.CharField(max_length=123)),
                ('phone', models.CharField(max_length=12)),
                ('msg', models.CharField(max_length=123)),
                ('date', models.DateField()),
            ],
        ),
    ]
