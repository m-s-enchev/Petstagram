# Generated by Django 4.2.2 on 2023-06-19 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='like_photo',
            new_name='to_photo',
        ),
    ]
