# Generated by Django 4.1.2 on 2022-10-15 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_is_actual'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='time_finish',
            field=models.DateTimeField(null=True),
        ),
    ]
