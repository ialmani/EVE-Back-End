# Generated by Django 3.1.3 on 2021-04-10 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoom', '0002_zoom_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zoom',
            name='password',
            field=models.CharField(max_length=120),
        ),
    ]
