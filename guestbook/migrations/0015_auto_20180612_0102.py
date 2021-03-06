# Generated by Django 2.0.6 on 2018-06-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0014_auto_20180612_0052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footerlinks',
            old_name='linkedin',
            new_name='linkedin_social_link',
        ),
        migrations.RemoveField(
            model_name='footerlinks',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='footerlinks',
            name='twitter',
        ),
        migrations.AddField(
            model_name='footerlinks',
            name='fb_social_link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='footerlinks',
            name='twitter_social_link',
            field=models.URLField(null=True),
        ),
    ]
