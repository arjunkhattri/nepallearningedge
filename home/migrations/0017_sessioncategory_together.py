# Generated by Django 2.2.8 on 2020-08-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_blognewsimages_sessionimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessioncategory',
            name='together',
            field=models.BooleanField(default=False),
        ),
    ]
