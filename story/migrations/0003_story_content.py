# Generated by Django 4.0.3 on 2023-02-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_alter_story_options_remove_story_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
