# Generated by Django 5.0.3 on 2024-05-04 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_remove_employee_department'),
    ]

    operations = [
        migrations.DeleteModel(
            name='department',
        ),
    ]
