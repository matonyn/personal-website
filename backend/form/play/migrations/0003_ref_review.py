# Generated by Django 4.2.6 on 2023-10-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0002_rename_company_ref_connection_ref_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='ref',
            name='review',
            field=models.BooleanField(default=False),
        ),
    ]
