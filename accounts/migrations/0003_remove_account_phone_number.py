# Generated by Django 3.2.5 on 2021-07-03 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='phone_number',
        ),
    ]
