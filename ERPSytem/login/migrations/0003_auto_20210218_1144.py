# Generated by Django 3.1.5 on 2021-02-18 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_holiday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='holiday',
            old_name='date',
            new_name='date_of_event',
        ),
    ]
