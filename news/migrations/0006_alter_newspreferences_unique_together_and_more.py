# Generated by Django 4.0.3 on 2023-05-27 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_userpreferences_unique_together_and_more'),
        ('news', '0005_alter_tag_background_color'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='newspreferences',
            unique_together={('news', 'preference')},
        ),
        migrations.AlterUniqueTogether(
            name='newstags',
            unique_together={('news', 'tag')},
        ),
    ]
