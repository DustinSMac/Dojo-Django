# Generated by Django 2.2 on 2021-05-15 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_dojos_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ninjas',
            old_name='dojo_ID',
            new_name='dojo',
        ),
    ]