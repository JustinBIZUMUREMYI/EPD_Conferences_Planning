# Generated by Django 5.0.6 on 2024-06-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0011_previousphotos'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='activity',
            field=models.TextField(default='', max_length=10000),
        ),
    ]
