# Generated by Django 4.2.2 on 2023-06-18 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.photo')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time_of_publication', models.DateTimeField(auto_created=True)),
                ('text', models.TextField(max_length=300)),
                ('to_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.photo')),
            ],
        ),
    ]