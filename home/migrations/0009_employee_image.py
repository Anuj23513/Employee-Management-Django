# Generated by Django 5.0.3 on 2024-04-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_employee_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default=11, upload_to=''),
            preserve_default=False,
        ),
    ]
