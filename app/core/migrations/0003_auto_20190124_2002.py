# Generated by Django 2.1.5 on 2019-01-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_calendar_event_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='visitors',
            field=models.ManyToManyField(to='core.Group'),
        ),
    ]
