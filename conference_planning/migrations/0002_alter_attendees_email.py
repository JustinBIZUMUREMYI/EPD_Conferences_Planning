# Generated by Django 5.0.4 on 2024-06-07 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendees',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
