# Generated by Django 4.2.5 on 2024-08-27 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]
