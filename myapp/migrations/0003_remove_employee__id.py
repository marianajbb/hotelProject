# Generated by Django 5.1.6 on 2025-03-21 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_employee__id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='_id',
        ),
    ]
