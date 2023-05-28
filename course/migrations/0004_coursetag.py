# Generated by Django 4.0.3 on 2023-05-28 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_newspreferences_unique_together_and_more'),
        ('course', '0003_userviewedlessons_userpassedlessons'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='course.course')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.tag')),
            ],
        ),
    ]
