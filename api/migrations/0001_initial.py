# Generated by Django 5.1.7 on 2025-04-16 09:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargingStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('operator', models.CharField(max_length=100)),
                ('available_ports', models.IntegerField(default=2)),
                ('charging_types', models.JSONField()),
                ('power_output', models.CharField(max_length=50)),
                ('price_per_kwh', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(decimal_places=2, default=4.5, max_digits=3)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(max_length=100)),
                ('station_name', models.CharField(max_length=255)),
                ('booking_time', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField(help_text='Duration in hours')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('charger_type', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
