#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

STATUS = (
    ('STABLE','stable' ),
    ('RC', 'rc'),
    ('BETA','beta'),
    ('ALPHA', 'alpha'),
    ('SANDBOX','sandbox')
)

class Service(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    service_id = models.IntegerField(max_length=6)
    url_interne = models.CharField(max_length=100)
    url_externe = models.CharField(max_length=100)
    mep = models.DateField(null=True, blank=True)
    dev = models.DateField(null=True, blank=True)
    client = models.CharField(max_length=20, null=True, blank=True)
    cdp = models.CharField(max_length=20, null=True, blank=True)
    status = models.ForeignKey('Status')
    #FEEDS
    
    feeds = models.ManyToManyField('Feed', blank=True, null=True, through='FeedToService')
    
    
    
    def __unicode__(self):
        return "%s " %(self.nom)
    
class Status(models.Model):
    nom = models.CharField(max_length=25) 
    
    class Meta:
        verbose_name_plural = "Status"
    
    def __unicode__(self):
        return "%s " %(self.nom)    
    

class Feed(models.Model):

    nom = models.CharField(max_length=25)
    path = models.CharField(max_length=250)
    indexeur = models.ForeignKey('Indexeur')
    repondeur = models.ManyToManyField('Repondeur') 
    #SONDES
    freshness = models.ForeignKey('Freshness')
    
    class Meta:
        verbose_name_plural = "Feeds"
    
    def __unicode__(self):
        return "%s" %(self.nom)
    
    
class FeedToService(models.Model):
    service = models.ForeignKey('Service')
    feed = models.ForeignKey('Feed')    
    
    
class Indexeur(models.Model):
    nom = models.CharField(max_length=25) 
    
    def __unicode__(self):
        return "%s " %(self.nom)
    
class Repondeur(models.Model):
    nom = models.CharField(max_length=25) 
    
    def __unicode__(self):
        return "%s " %(self.nom)    
    
    

    
    
#sondes    
class Freshness(models.Model):
    monitoring = models.BooleanField(default=False) 
    warning_threshold = models.IntegerField(max_length=4)
    critical_threshold = models.IntegerField(max_length=4)
    class Meta:
        verbose_name_plural = "Freshness"
    
    def __unicode__(self):
        return "%s - %s - %s" %(self.warning_threshold, self.critical_threshold, self.monitoring)
#        return (self.warning_threshold, self.critical_threshold, self.monitoring)

