# Generated by Django 5.0.6 on 2024-06-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0014_alter_agenda_options_agenda_day_event_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='day_event',
            field=models.CharField(default='', max_length=100),
        ),
    ]