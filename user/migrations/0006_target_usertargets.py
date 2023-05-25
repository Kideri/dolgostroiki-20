# Generated by Django 4.2.1 on 2023-05-25 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_preference_userpreferences'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('code', models.CharField(help_text='Name for server', max_length=31, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name for user', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserTargets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='user.target')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
