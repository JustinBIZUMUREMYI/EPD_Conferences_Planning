# Generated by Django 5.0.6 on 2024-06-22 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0029_booksponsorship_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booth',
            name='status',
            field=models.CharField(choices=[('book', 'Book'), ('booked', 'Booked')], default='book', max_length=10),
        ),
        migrations.AlterField(
            model_name='booksponsorship',
            name='status',
            field=models.CharField(choices=[('register', 'Register'), ('registered', 'Registered')], default='register', max_length=10),
        ),
    ]
