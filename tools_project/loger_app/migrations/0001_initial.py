# Generated by Django 4.2.7 on 2023-11-11 08:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(10)])),
                ('description', models.TextField()),
            ],
        ),
    ]
