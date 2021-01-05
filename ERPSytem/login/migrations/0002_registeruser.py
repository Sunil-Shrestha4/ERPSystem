# Generated by Django 3.1.4 on 2020-12-27 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('email', models.EmailField(max_length=225, unique=True)),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('phone_numver', models.IntegerField()),
                ('position', models.CharField(max_length=225)),
                ('department', models.CharField(max_length=225)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
            ],
        ),
    ]