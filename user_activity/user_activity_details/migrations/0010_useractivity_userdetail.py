# Generated by Django 3.0.8 on 2020-07-07 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_activity_details', '0009_auto_20200707_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.CharField(editable=False, max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('time_zone', models.CharField(max_length=21)),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_activity_details.UserDetail')),
            ],
            options={
                'db_table': 'user_activity',
            },
        ),
    ]