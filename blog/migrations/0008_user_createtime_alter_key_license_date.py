# Generated by Django 5.1a1 on 2024-06-11 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_key_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='createtime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='license_date',
            field=models.DateTimeField(null=True),
        ),
    ]
