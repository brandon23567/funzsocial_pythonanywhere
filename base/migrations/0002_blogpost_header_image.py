# Generated by Django 4.2.9 on 2024-01-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='header_images/'),
        ),
    ]
