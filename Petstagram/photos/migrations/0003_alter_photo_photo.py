# Generated by Django 4.2.2 on 2023-07-21 17:04

import Petstagram.photos.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_photo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='images', validators=[Petstagram.photos.validator.validate_file_size]),
        ),
    ]
