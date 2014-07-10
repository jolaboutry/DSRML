#-*- coding: utf-8 -*-
from django.db import models
import blog.sondes as sondes

# Create your models here.

TYPE = (
    ('AFS@Store','AFS@Store' ),
    ('ft', 'Fluid Topics'),
    ('afs','AFS'),
    ('licence', 'Licence')
)

STATUS = (
    ('stable','STABLE' ),
    ('rc', 'RC'),
    ('beta','BETA'),
    ('alpha','ALPHA')
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
    type = models.CharField(max_length = 25, choices=TYPE)
    #FEEDS
    feeds = models.ManyToManyField('Feed', blank=True, null=True, through='FeedToService')
   
    
    def __unicode__(self):
        return "%s " %(self.nom)
    
class Status(models.Model):
    nom = models.CharField(max_length=8, choices=STATUS) 
    
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
    page_range = models.ForeignKey('Page_range')
    sanity = models.ForeignKey('Sanity')
    last_indexation = models.ForeignKey('Last_indexation')
    result_count = models.ForeignKey('Result_count')

    
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
    
    

    
    

