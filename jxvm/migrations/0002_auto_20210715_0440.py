# Generated by Django 3.2.5 on 2021-07-15 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jxvm', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]