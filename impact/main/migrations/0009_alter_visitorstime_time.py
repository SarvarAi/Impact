# Generated by Django 4.2.1 on 2023-05-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_visitorstime_test_alter_visitorstime_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitorstime',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
