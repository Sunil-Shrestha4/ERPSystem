# Generated by Django 3.1.4 on 2020-12-27 07:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_remove_leave_emp_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='emp_name',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
    ]
