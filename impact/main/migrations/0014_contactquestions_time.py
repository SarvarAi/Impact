# Generated by Django 4.2.1 on 2023-06-01 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_contactquestions_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactquestions',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
