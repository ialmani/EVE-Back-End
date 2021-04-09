# Generated by Django 3.1.4 on 2021-04-09 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210409_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='account_type',
        ),
        migrations.AddField(
            model_name='user',
            name='is_sponsor',
            field=models.BooleanField(default=False),
        ),
    ]
