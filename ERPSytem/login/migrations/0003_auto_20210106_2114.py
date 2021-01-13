# Generated by Django 3.1.4 on 2021-01-06 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20210106_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='your address', max_length=225),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(default='Employee', on_delete=django.db.models.deletion.CASCADE, to='login.department'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='your first name', max_length=225),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='your last name', max_length=225),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='MEDIA_ROOT'),
        ),
    ]
