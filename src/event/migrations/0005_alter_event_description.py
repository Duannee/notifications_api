# Generated by Django 5.1.1 on 2024-11-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_remove_event_end_time_remove_event_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]