# Generated by Django 2.0.6 on 2018-06-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0007_auto_20180605_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='linkedin_social_link',
            field=models.URLField(),
        ),
    ]
