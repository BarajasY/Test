# Generated by Django 4.1.7 on 2023-03-15 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='story_content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='story',
            name='story_title',
            field=models.TextField(default=''),
        ),
    ]