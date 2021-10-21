# Generated by Django 3.0.14 on 2021-09-25 21:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20210925_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitionparticipation',
            name='division_num',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
