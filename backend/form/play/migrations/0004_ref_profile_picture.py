# Generated by Django 4.2.6 on 2023-10-15 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0003_ref_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='ref',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
