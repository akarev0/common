# Generated by Django 3.0.1 on 2020-01-26 18:18

from django.db import migrations


OBJECTS_TO_CREATE = 5
PERSONS_TO_CREATE = ['', '', '', '', '']


def generate_initial_data(apps, schema_editor):
    Tenant = apps.get_model('mycore', 'Tenant')
    Room = apps.get_model('mycore', 'Room')
    Key = apps.get_model('mycore', 'Key')
    for i in range(OBJECTS_TO_CREATE):
        apartment = Room(room_number=i)
        apartment.save()
        key = Key(room=apartment)
        key.save()
        tenant = Tenant(first_name=f'test_person_name{i}')
        tenant.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mycore', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_initial_data),
    ]
