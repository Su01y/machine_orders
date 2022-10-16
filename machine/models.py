from django.db import models


class Machine(models.Model):
    park = models.CharField(max_length=200)
    characters = models.TextField()
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    address = models.TextField(null=True)
    is_free = models.BooleanField(default=True)

    class Meta:
        db_table = 'Machine'

    def __str__(self) -> str:
        return self.park


