# Generated by Django 3.2.5 on 2021-08-11 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20210811_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='niveau',
            name='filiere',
        ),
    ]
