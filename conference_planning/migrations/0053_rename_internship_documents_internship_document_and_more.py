# Generated by Django 5.0.6 on 2024-10-18 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference_planning', '0052_internship_documents_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='internship_documents',
            new_name='internship_document',
        ),
        migrations.RenameField(
            model_name='internship_document',
            old_name='company',
            new_name='company_name',
        ),
    ]