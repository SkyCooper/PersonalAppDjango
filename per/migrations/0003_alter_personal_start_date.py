# Generated by Django 4.1.4 on 2023-01-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('per', '0002_personal_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
