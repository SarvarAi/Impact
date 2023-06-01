# Generated by Django 4.2.1 on 2023-05-31 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_visitorstime_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=510)),
                ('message', models.TextField()),
                ('is_answered', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Contact question',
                'verbose_name_plural': 'Contact questions',
            },
        ),
    ]
