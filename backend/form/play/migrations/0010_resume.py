# Generated by Django 4.2.6 on 2023-10-17 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0009_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pdf', models.FileField(blank=True, upload_to='Users/madinadairova/Documents/my_website/backend/media')),
            ],
        ),
    ]