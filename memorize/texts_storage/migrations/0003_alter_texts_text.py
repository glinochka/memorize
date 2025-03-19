# Generated by Django 5.1.6 on 2025-03-19 21:31

import django.core.validators
import texts_storage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texts_storage', '0002_alter_texts_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='text',
            field=models.FileField(upload_to=texts_storage.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]
