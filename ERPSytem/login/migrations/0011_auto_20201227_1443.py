# Generated by Django 3.1.4 on 2020-12-27 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_registeruser_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='file',
            field=models.FileField(blank=True, upload_to='pics'),
        ),
    ]