# Generated by Django 4.0.3 on 2023-05-26 11:22

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='background_color',
            field=colorfield.fields.ColorField(default='#000000', image_field=None, max_length=18, samples=None),
        ),
    ]