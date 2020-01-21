# Generated by Django 3.0.1 on 2020-01-21 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=5, verbose_name='room_number')),
                ('maximum_number_of_guest', models.CharField(blank=True, max_length=2, null=True, verbose_name='max_guest')),
            ],
        ),
        migrations.AddField(
            model_name='tenant',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET, to='mycore.Room'),
        ),
    ]