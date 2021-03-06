# Generated by Django 4.0.4 on 2022-04-16 17:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_alter_post_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendship',
            old_name='friend',
            new_name='following',
        ),
        migrations.RenameField(
            model_name='friendship',
            old_name='creator',
            new_name='root',
        ),
        migrations.RenameField(
            model_name='friendship',
            old_name='created',
            new_name='time_created',
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 16, 17, 43, 36, 205707, tzinfo=utc)),
        ),
    ]
