# Generated by Django 5.1.6 on 2025-04-03 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texts_storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='many_words',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='words',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
