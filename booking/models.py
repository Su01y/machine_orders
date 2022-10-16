import datetime as dt

from django.db import models


class Booking(models.Model):
    time_start = models.DateTimeField()
    description = models.TextField()
    address = models.TextField(null=True)
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE)
    is_actual = models.BooleanField(default=True)
    machine = models.ForeignKey('machine.Machine', on_delete=models.CASCADE)
    hours = models.TimeField(null=True)

