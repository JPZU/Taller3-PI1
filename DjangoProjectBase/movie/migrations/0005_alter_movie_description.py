# Generated by Django 5.0.1 on 2024-04-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(max_length=1500),
        ),
    ]
