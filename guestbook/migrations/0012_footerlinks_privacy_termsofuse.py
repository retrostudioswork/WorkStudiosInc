# Generated by Django 2.0.6 on 2018-06-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0011_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TermsOfUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', models.TextField()),
            ],
        ),
    ]
