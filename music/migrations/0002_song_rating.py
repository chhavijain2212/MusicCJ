# Generated by Django 2.0.2 on 2018-02-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
