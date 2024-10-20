# Generated by Django 5.0.6 on 2024-06-17 19:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0023_sponsorships'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='sponsorship',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='conference_planning.sponsorships'),
        ),
        migrations.AddField(
            model_name='sponsorships',
            name='file',
            field=models.FileField(default='', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='sponsorships',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
