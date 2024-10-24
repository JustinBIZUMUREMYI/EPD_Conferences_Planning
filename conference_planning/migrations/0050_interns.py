# Generated by Django 5.0.6 on 2024-10-17 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0049_attendees_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=250)),
                ('Email', models.EmailField(max_length=254)),
                ('ID_number', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=20)),
                ('Country', models.CharField(max_length=100)),
                ('University', models.CharField(max_length=100)),
                ('Education_level', models.CharField(choices=[('advanced diploma', 'Advanced Diploma'), ('bachelor degree', 'Bachelor Degree'), ('master degree', 'Master Degree')], default='choose your category', max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
                ('Graduation_date', models.DateField()),
                ('Degree', models.FileField(upload_to='uploads/')),
                ('Resume', models.FileField(upload_to='uploads/')),
                ('Other_documents', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('Host_Company', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='conference_planning.testimonial')),
            ],
            options={
                'verbose_name_plural': 'Interns',
            },
        ),
    ]
