# Generated by Django 3.0.8 on 2020-08-09 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200808_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='ready',
        ),
        migrations.AddField(
            model_name='character',
            name='death',
            field=models.TextField(default='alive'),
        ),
    ]