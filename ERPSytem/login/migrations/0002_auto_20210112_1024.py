# Generated by Django 3.1.5 on 2021-01-12 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.department', unique=True),
        ),
    ]