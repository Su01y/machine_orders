# Generated by Django 4.1.2 on 2022-10-15 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_booking_time_finish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='time_finish',
        ),
    ]
