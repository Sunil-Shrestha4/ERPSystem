# Generated by Django 3.1.4 on 2020-12-27 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20201227_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='file',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]
