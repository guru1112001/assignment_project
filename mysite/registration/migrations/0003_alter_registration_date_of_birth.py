# Generated by Django 4.2.8 on 2024-02-04 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_registration_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
