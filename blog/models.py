#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.



class Service(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    service_id = models.IntegerField(max_length=6, primary_key=True)
    status = models.ForeignKey('Status')
    indexeur = models.ForeignKey('Indexeur')
    url_interne = models.CharField(max_length=100)
    url_externe = models.CharField(max_length=100)
    mep = models.DateField(null=True)
    dev = models.DateField(null=True)
       

    def __unicode__(self):
        return "%s " %(self.nom)
    
class Status(models.Model):
    nom = models.CharField(max_length=10) 
    
    def __unicode__(self):
        return "%s " %(self.nom)
    
class Indexeur(models.Model):
    nom = models.CharField(max_length=25) 
    
    def __unicode__(self):
        return "%s " %(self.nom)

