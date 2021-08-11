# Generated by Django 2.2.8 on 2020-07-12 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200711_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialSitesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.URLField(blank=True, max_length=500)),
                ('instagram_link', models.URLField(blank=True, max_length=500)),
                ('twitter_link', models.URLField(blank=True, max_length=500)),
                ('youtube_link', models.URLField(blank=True, max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='GalleryImage',
        ),
        migrations.DeleteModel(
            name='GalleryPosts',
        ),
    ]