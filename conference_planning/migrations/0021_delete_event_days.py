# Generated by Django 5.0.6 on 2024-06-16 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0020_remove_agenda_day_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event_days',
        ),
    ]
