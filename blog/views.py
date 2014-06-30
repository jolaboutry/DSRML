#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Count
from blog.models import Service, Indexeur, Feed, FeedToService

# Create your views here.
def accueil(request):
    """<h1>Bienvenue sur DSRML !</h1>
            <p>Liste des services </p>"""
    services = Service.objects.all()
    indexeurs = Indexeur.objects.all()
    #stables

    return render(request, 'blog/accueil.html', {'all_services':services,'servs':indexeurs})   



            
def lire(request, id):
    """afficher un service complet"""
    service = get_object_or_404(Service, id=id)
   
    feeds = FeedToService.objects.filter(service_id=id)
    values = Feed.objects.filter(id__in=feeds).select_related()
  
    return render(request, 'blog/lire.html', {'service':service, 'feeds':values})

def indexeur(request, id):
    """list les indexeurs"""
    
    indexeur = get_object_or_404(Indexeur, id=id)
    return render(request, 'blog/indexeur.html', {'indexeur':indexeur})

def stable(request):
    """list les services stables"""
    return render(request, 'blog/stable.html', )

def rc(request):
    """list les services rc"""
    return render(request, 'blog/rc.html', )

def beta(request):
    """list les services beta"""
    return render(request, 'blog/beta.html', )


     
