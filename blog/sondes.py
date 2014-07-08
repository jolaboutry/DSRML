#-*- coding: utf-8 -*-
from django.db import models


class Last_indexation(models.Model):
    monitoring = models.BooleanField(default=False)

    class Meta: 
        verbose_name_plural = "Last_indexation"
            
    def __unicode__(self):
        return "%s " %(self.monitoring)

class Result_count(models.Model):
    monitoring = models.BooleanField(default=False) 
    afs_query = models.CharField(max_length=15)
    afs_feed = models.CharField(max_length=15)
    warning_threshold = models.IntegerField(max_length=3)
    critical_threshold = models.IntegerField(max_length=3)
    
    class Meta:
        verbose_name_plural = "Results_count"
    
    def __unicode__(self):
        return "%s - %s - %s - %s - %s" %(self.afs_query, self.afs_feed, self.warning_threshold, self.critical_threshold, self.monitoring)

   
class Freshness(models.Model):
    monitoring = models.BooleanField(default=False) 
    warning_threshold = models.IntegerField(max_length=4)
    critical_threshold = models.IntegerField(max_length=4)
    class Meta:
        verbose_name_plural = "Freshness"
    
    def __unicode__(self):
        return "%s - %s - %s" %(self.warning_threshold, self.critical_threshold, self.monitoring)

class Page_range(models.Model):
    monitoring = models.BooleanField(default=False) 
    critical_min_threshold = models.IntegerField(max_length=5)
    warning_min_threshold = models.IntegerField(max_length=5)
    warning_max_threshold = models.IntegerField(max_length=6)
    critical_max_threshold = models.IntegerField(max_length=6)
   
    class Meta:
        verbose_name_plural = "Pages_range"
    
    def __unicode__(self):
        return "%s - %s - %s - %s - %s " %(self.critical_min_threshold, self.warning_min_threshold, self.warning_max_threshold, self.critical_max_threshold, self.monitoring)


class Sanity(models.Model):
    monitoring = models.BooleanField(default=False) 
    warning_threshold = models.IntegerField(max_length=3, default=95)
    critical_threshold = models.IntegerField(max_length=3, default=90)
    class Meta:
        verbose_name_plural = "Sanity"
    
    def __unicode__(self):
        return "%s - %s - %s" %(self.warning_threshold, self.critical_threshold, self.monitoring)
    
class Acp(models.Model):
    monitoring = models.BooleanField(default=False) 
    keyword = models.CharField(max_length=15)
    result = models.CharField(max_length=15)
    
    class Meta:
        verbose_name_plural = "Acps"
    
    def __unicode__(self):
        return "%s - %s - %s " %(self.keyword, self.result, self.monitoring)

    