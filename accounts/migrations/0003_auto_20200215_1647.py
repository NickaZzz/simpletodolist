# Generated by Django 3.0.2 on 2020-02-15 16:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='uid',
            field=models.CharField(default=uuid.uuid4, max_length=40),
        ),
    ]