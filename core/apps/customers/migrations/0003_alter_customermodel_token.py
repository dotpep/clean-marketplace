# Generated by Django 5.0.3 on 2024-03-18 22:43

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customermodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='token',
            field=models.CharField(default=uuid.uuid4, max_length=255, unique=True, verbose_name='User Auth Token'),
        ),
    ]