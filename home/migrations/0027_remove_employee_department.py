# Generated by Django 5.0.3 on 2024-05-04 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_alter_department_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
    ]
