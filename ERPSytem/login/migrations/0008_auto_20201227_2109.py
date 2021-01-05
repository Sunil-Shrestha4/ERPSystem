# Generated by Django 3.1.4 on 2020-12-27 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20201227_1635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={},
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='checkin',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='checkout',
        ),
        migrations.AddField(
            model_name='attendance',
            name='choices',
            field=models.CharField(choices=[('CI', 'checkin'), ('CO', 'checkout')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]
