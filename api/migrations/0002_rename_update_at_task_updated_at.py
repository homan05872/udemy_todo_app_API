# Generated by Django 4.2.7 on 2023-11-27 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
