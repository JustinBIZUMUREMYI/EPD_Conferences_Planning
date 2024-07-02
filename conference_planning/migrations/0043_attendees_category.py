# Generated by Django 5.0.6 on 2024-06-28 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0042_accessory_remove_bookbooth_category_bookaccessory'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendees',
            name='category',
            field=models.CharField(choices=[('organizer', 'Organizer'), ('delegate', 'Delegate'), ('exhibitor', 'Exhibitor'), ('student', 'Student'), ('media', 'Media')], default='organizer', max_length=100),
        ),
    ]