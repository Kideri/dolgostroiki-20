# Generated by Django 4.0.3 on 2023-05-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_question_correct_answer_reaction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='score',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
