# Generated by Django 2.0.2 on 2018-05-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_app', '0003_auto_20180521_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
            ],
        ),
        migrations.DeleteModel(
            name='archery_boards',
        ),
    ]