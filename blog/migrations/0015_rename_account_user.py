# Generated by Django 5.1a1 on 2024-06-11 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_rename_user_account'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='User',
        ),
    ]
