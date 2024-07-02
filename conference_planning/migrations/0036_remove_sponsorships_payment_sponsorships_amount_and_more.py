# Generated by Django 5.0.6 on 2024-06-25 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0035_sponsorships_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsorships',
            name='payment',
        ),
        migrations.AddField(
            model_name='sponsorships',
            name='amount',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='Amount',
        ),
    ]