# Generated by Django 5.0.6 on 2024-06-26 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0038_remove_booksponsorship_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksponsorship',
            name='status',
            field=models.CharField(choices=[('registering', 'Registering'), ('registered', 'Registered')], default='register', max_length=100),
        ),
    ]
