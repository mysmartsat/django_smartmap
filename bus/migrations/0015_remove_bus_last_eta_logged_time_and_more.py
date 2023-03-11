# Generated by Django 4.0.5 on 2023-03-11 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0014_busarrivallog_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='last_eta_logged_time',
        ),
        migrations.AddField(
            model_name='bus',
            name='eta_log_time_counter',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='busarrivallogentry',
            name='api_response_value',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='busarrivallogentry',
            name='stop_skipped_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='busarrivallogentry',
            name='time_stamp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]