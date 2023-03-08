# Generated by Django 4.0.5 on 2023-01-02 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0013_bus_seat_availability'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusArrivalLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.CharField(max_length=100)),
                ('route_id', models.PositiveSmallIntegerField(default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='transit_log_id',
            new_name='arrival_log_id',
        ),
        migrations.AddField(
            model_name='bus',
            name='last_eta_logged_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='bus',
            name='latest_route_stop_index',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='BusArrivalLogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('time_stamp', models.DateTimeField(blank=True, default=None, null=True)),
                ('bus_stop_id', models.PositiveIntegerField(default=None)),
                ('estimated_arrival_time', models.CharField(max_length=100)),
                ('actual_arrival_time', models.CharField(max_length=100)),
                ('bus_arrival_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.busarrivallog')),
            ],
        ),
    ]