# Generated by Django 2.0.6 on 2018-06-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0015_auto_20180612_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerlinks',
            name='fb_social_link',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='footerlinks',
            name='linkedin_social_link',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='footerlinks',
            name='twitter_social_link',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
