# Generated by Django 4.2.2 on 2023-07-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_petstagramuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstagramuser',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('do not show', 'Do not show')], max_length=11),
        ),
    ]
