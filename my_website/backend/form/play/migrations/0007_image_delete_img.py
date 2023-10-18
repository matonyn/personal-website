# Generated by Django 4.2.6 on 2023-10-15 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0006_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='media')),
            ],
        ),
        migrations.DeleteModel(
            name='img',
        ),
    ]