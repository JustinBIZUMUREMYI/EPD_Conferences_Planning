# Generated by Django 5.0.6 on 2024-06-13 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0008_rename_names_testimonial_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='name',
            new_name='names',
        ),
    ]
