# Generated by Django 2.2.6 on 2019-11-25 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_auto_20191120_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
        migrations.RemoveField(
            model_name='document',
            name='scores',
        ),
    ]
