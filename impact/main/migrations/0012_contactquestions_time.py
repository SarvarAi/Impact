# Generated by Django 4.2.1 on 2023-06-01 03:55

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_contactquestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactquestions',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now().isoformat()),
            preserve_default=False,
        ),
    ]
