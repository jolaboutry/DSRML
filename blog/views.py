#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from blog.models import Service

# Create your views here.
def accueil(request):
    """<h1>Bienvenue sur DSRML !</h1>
            <p>Liste des services </p>"""
    services = Service.objects.all()
    return render(request, 'blog/accueil.html', {'all_services':services})        
            
            
def lire(request, id):
    """afficher un service complet"""
    try:
        service = Service.objects.get(id=id)
    except Service.DoesNotExist:
        raise Http404
    
    return render(request, 'blog/lire.html', {'service':service})     
            
