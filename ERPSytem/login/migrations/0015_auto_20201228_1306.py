# Generated by Django 3.1.4 on 2020-12-28 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20201227_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='pics')),
            ],
        ),
        migrations.RemoveField(
            model_name='registeruser',
            name='file',
        ),
    ]
