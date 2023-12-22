# Generated by Django 4.2.6 on 2023-10-18 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0011_delete_image_ref_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ref',
            name='email_adress',
            field=models.CharField(default='name.surname@gmail.com', max_length=200),
        ),
        migrations.AddField(
            model_name='ref',
            name='linkedin_url',
            field=models.CharField(default='linkein/url', max_length=200),
        ),
        migrations.AlterField(
            model_name='ref',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]