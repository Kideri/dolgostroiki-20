# Generated by Django 4.0.3 on 2023-05-26 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('levels', '0004_alter_config_exp_alter_userlevel_total_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlevel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='level', to=settings.AUTH_USER_MODEL),
        ),
    ]