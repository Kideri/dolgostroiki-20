# Generated by Django 4.0.3 on 2023-05-26 16:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0003_alter_config_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='exp',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='userlevel',
            name='total_exp',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
