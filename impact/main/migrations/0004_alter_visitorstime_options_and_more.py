# Generated by Django 4.2.1 on 2023-05-21 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_visitorstime_visitor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visitorstime',
            options={'verbose_name': 'Visited time', 'verbose_name_plural': 'Visited times'},
        ),
        migrations.RenameField(
            model_name='visitorstime',
            old_name='visitor',
            new_name='Visitors',
        ),
    ]