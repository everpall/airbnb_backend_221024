# Generated by Django 4.1.2 on 2022-11-19 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0005_rename_created_experience_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='event_duration',
            field=models.DurationField(default=datetime.timedelta(seconds=7200)),
        ),
    ]
