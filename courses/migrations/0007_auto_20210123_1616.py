# Generated by Django 3.1.5 on 2021-01-23 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_usersstats_pupil'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'permissions': (('can_mark_returned', 'Set course as returned'),)},
        ),
    ]
