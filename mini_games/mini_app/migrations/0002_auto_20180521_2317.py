# Generated by Django 2.0.2 on 2018-05-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archery_boards',
            name='score',
            field=models.IntegerField(blank=True),
        ),
    ]
