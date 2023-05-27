# Generated by Django 4.0.3 on 2023-05-27 15:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0004_useranswers'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='useranswers',
            unique_together={('user', 'question')},
        ),
    ]
