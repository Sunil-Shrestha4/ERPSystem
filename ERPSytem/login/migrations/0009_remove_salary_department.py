# Generated by Django 3.1.5 on 2021-01-17 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20210117_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='department',
        ),
    ]
