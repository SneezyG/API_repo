# Generated by Django 4.0.3 on 2022-06-16 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0013_alter_users_mail_alter_users_mug_shot_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='secrete_key',
            new_name='secret_key',
        ),
        
        migrations.AddField(
            model_name='users',
            name='project_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]