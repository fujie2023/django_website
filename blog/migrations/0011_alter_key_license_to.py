# Generated by Django 5.1a1 on 2024-06-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_key_license_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='license_to',
            field=models.CharField(max_length=32),
        ),
    ]
