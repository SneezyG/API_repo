# Generated by Django 4.0.3 on 2022-06-12 21:14

from django.db import migrations, models
import elements.models


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0011_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='secrete_key',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='users',
            name='mug_shot',
            field=models.ImageField(blank=True, upload_to=elements.models.path),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='project_key',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='users',
            name='user',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]