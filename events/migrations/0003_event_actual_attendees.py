# Generated by Django 5.1.1 on 2024-10-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='actual_attendees',
            field=models.IntegerField(default=0),
        ),
    ]
