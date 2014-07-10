from blog.models import Service, Indexeur

def getInfos(request):
    """<h1>Bienvenue sur DSRML !</h1>
            <p>Liste des services </p>"""
    services = Service.objects.all()
    indexeurs = Indexeur.objects.all()
    #stables
    servicesStable = Service.objects.filter(status__nom__contains=u"STABLE")
    countServicesStable = Service.objects.filter(status__nom__contains=u"STABLE").count()
    servicesStable5 = Service.objects.filter(status__nom__contains=u"STABLE").order_by('mep').reverse()[:5]
    #rc
    servicesRc = Service.objects.filter(status__nom__contains=u"RC")
    countServicesRc = Service.objects.filter(status__nom__contains=u"RC").count()
    servicesRc5 = Service.objects.filter(status__nom__contains=u"RC")[:5]
    #beta
    servicesBeta = Service.objects.filter(status__nom__contains=u"BETA")
    countServicesBeta = Service.objects.filter(status__nom__contains=u"BETA").count()
    servicesBeta5 = Service.objects.filter(status__nom__contains=u"BETA")[:5]
    
    nbStore = Service.objects.filter(type=u"AFS@Store").count()
    nbFT = Service.objects.filter(type=u"FLUID TOPICS").count()
    nbAFS = Service.objects.filter(type=u"AFS").count()
    nbLicence = Service.objects.filter(type=u"LICENCE").count()
    
    
    
    return {'all_services':services,'servs':indexeurs,
                                                 'servicesStable':servicesStable, '5firstStable':servicesStable5,'nbStable':countServicesStable,
                                                 'servicesRc':servicesRc, '5firstRc':servicesRc5,'nbRc':countServicesRc,
                                                 'servicesBeta':servicesBeta, '5firstBeta':servicesBeta5,'nbBeta':countServicesBeta,
                                                 'nbStore':nbStore, 'nbFT':nbFT, 'nbAFS': nbAFS, 'nbLicence':nbLicence}