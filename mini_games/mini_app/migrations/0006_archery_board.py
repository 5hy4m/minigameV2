# Generated by Django 2.0.2 on 2018-05-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_app', '0005_auto_20180525_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='archery_board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('score', models.CharField(max_length=264)),
            ],
        ),
    ]
