# Generated by Django 5.1.6 on 2025-04-03 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('texts_storage', '0002_many_words_rate_words_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='words',
            old_name='word',
            new_name='words',
        ),
    ]
