# Generated by Django 4.2.9 on 2024-01-10 16:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_blogpost_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='header_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Images'),
        ),
    ]