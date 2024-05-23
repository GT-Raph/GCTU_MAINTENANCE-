# Generated by Django 5.0.4 on 2024-05-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAINTENANCE', '0005_remove_maintenancerequest_solved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancerequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=10),
        ),
    ]
