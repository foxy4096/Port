# Generated by Django 4.0.3 on 2023-02-19 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0005_alter_story_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Stories'},
        ),
        migrations.AddField(
            model_name='story',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='story.story'),
        ),
    ]