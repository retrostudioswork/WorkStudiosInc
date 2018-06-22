# Generated by Django 2.0.6 on 2018-06-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0019_auto_20180614_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footerlinks',
            name='fb_social_link',
        ),
        migrations.RemoveField(
            model_name='footerlinks',
            name='linkedin_social_link',
        ),
        migrations.RemoveField(
            model_name='footerlinks',
            name='twitter_social_link',
        ),
        migrations.AddField(
            model_name='footerlinks',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='footerlinks',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='footerlinks',
            name='twitter',
            field=models.URLField(blank=True),
        ),
    ]