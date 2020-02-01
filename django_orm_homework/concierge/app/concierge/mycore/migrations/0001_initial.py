# Generated by Django 3.0.1 on 2020-02-01 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('guests_number', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='mycore.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, verbose_name='First name')),
                ('last_name', models.CharField(max_length=250, verbose_name='Last name')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET, to='mycore.Room')),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_out_date', models.DateTimeField(null=True)),
                ('key_in_date', models.DateTimeField(auto_now_add=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mycore.Tenant')),
            ],
        ),
        migrations.AddIndex(
            model_name='tenant',
            index=models.Index(fields=['first_name', 'last_name'], name='mycore_tena_first_n_59e684_idx'),
        ),
        migrations.AddField(
            model_name='journal',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mycore.Key'),
        ),
    ]
