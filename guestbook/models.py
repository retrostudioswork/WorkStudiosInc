from django.db import models
from PIL import Image
from django.utils import timezone

class Team(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team/%y',blank=True)
    fb_social_link = models.URLField(null=True)
    twitter_social_link = models.URLField(null=True)
    linkedin_social_link = models.URLField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}'.format(self.name)

class Portfolio(models.Model):
    project_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/%Y/%m/%D',null=True)
    platform = models.CharField(max_length=80)
    #details = models.CharField(max_length=1000, blank=True)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}, {}'.format(self.project_name, self.category)

class About(models.Model):
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
       return '{}'.format(self.id)

class Services(models.Model):
    icon = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return '{}'.format(self.title)

class Clients(models.Model):
    logo = models.ImageField( upload_to='clients/logo',null=True)
    url = models.URLField()

    def __str__(self):
        return '{}'.format(self.id)

class Privacy(models.Model):
    policy = models.TextField()
    def __str__(self):
        return '{}'.format(self.id)


class TermsOfUse(models.Model):
    terms = models.TextField()

    def __str__(self):
        return '{}'.format(self.id)

class FooterLinks(models.Model):

    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    #fb_social_link = models.CharField(max_length=255, null=True)
    #twitter_social_link = models.CharField(max_length=255,null=True)
    #linkedin_social_link = models.CharField(max_length=255,null=True)

    def __str__(self):
        return '{}'.format(self.id)


