# Generated by Django 3.0.8 on 2020-07-07 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_activity_details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useractivity',
            old_name='user_id',
            new_name='user',
        ),
    ]
