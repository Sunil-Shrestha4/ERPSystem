# Generated by Django 3.1.4 on 2021-01-05 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='phone_number',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
