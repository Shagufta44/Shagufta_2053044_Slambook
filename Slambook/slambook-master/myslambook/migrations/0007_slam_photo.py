# Generated by Django 2.2.5 on 2019-09-21 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myslambook', '0006_remove_slam_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='slam',
            name='photo',
            field=models.FileField(default='photo.jpg', upload_to=''),
        ),
    ]
