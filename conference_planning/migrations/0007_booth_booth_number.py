# Generated by Django 5.0.6 on 2024-06-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0006_booth_panalist_partner_alter_testimonial_testimony'),
    ]

    operations = [
        migrations.AddField(
            model_name='booth',
            name='booth_number',
            field=models.CharField(default='', max_length=100),
        ),
    ]