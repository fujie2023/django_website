from django.db import models

# Create your models here.

class Demo(models.Model):
    car_num = models.CharField(max_length=32)
    park_name = models.CharField(max_length=32)
    jinru_date = models.CharField(max_length=32)
    chuqu_date = models.CharField(max_length=32)
    time = models.CharField(max_length=32)

class Key(models.Model):
    valid_key = models.CharField(max_length=100)
    is_used = models.BooleanField(default=False)
    valid_days = models.IntegerField(default=False)
    create_date = models.DateTimeField(null=True)
    license_date = models.DateTimeField(null=True)
    license_to = models.CharField(max_length=32)

class Computer(models.Model):
    baseboard_sn = models.CharField(max_length=100)
    bios_sn = models.CharField(max_length=100)
    cpu_id = models.CharField(max_length=100)
    cpu_name = models.CharField(max_length=100)
    cs_uuid = models.CharField(max_length=100)
    disk_sn = models.CharField(max_length=100)

class User(models.Model):
    company = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    createtime = models.DateTimeField(null=True)