# Generated by Django 5.0.6 on 2024-06-25 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0033_remove_sponsorships_amount_sponsorships_amounts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsorships',
            name='amounts',
        ),
    ]
