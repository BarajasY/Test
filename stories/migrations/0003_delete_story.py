# Generated by Django 4.1.7 on 2023-03-15 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_story_story_content_story_story_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Story',
        ),
    ]