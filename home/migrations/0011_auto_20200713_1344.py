# Generated by Django 2.2.8 on 2020-07-13 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_websiteinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='websiteinfo',
            old_name='NLE_info',
            new_name='Nle_info',
        ),
    ]
