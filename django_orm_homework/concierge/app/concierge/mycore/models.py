
from django.db import models

# Create your models here.
from django.db.models import OneToOneField, DO_NOTHING, DateTimeField, ForeignKey


class Tenant(models.Model):
    """
    Room's owner/tenant
    """
    first_name = models.CharField(
        'First name',
        max_length=250,
    )
    last_name = models.CharField(
        'Last name',
        max_length=250,
    )
    room = models.ForeignKey('Room', null=True,
                             on_delete=models.SET)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.fullname

    class Meta:
        ordering = ['first_name', 'last_name']
        indexes = [
            models.Index(fields=['first_name', 'last_name']),
        ]


class Room(models.Model):

    room_number = models.IntegerField()
    guests_number = models.IntegerField(null=True)


class Key(models.Model):
    room = OneToOneField(
        Room,
        primary_key=True,
        on_delete=DO_NOTHING
    )


class Journal(models.Model):
    key_out_date = DateTimeField(null=True)
    key_in_date = DateTimeField(auto_now_add=True)
    tenant = ForeignKey(Tenant, on_delete=DO_NOTHING)
    key = ForeignKey(Key, on_delete=DO_NOTHING)
