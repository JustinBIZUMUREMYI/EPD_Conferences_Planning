# Generated by Django 5.0.6 on 2024-06-25 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0032_amount_alter_sponsorships_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsorships',
            name='amount',
        ),
        migrations.AddField(
            model_name='sponsorships',
            name='amounts',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='conference_planning.amount'),
        ),
    ]
