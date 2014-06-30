from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
                       url(r'^$', 'accueil'),
                       url(r'^service/(?P<id>\d+)$', 'lire'),
                       url(r'^indexeur/(?P<id>\d+)$', 'indexeur'),
                       url(r'^service/stable/', 'stable'),
                       url(r'^service/rc/', 'rc'),
                       url(r'^service/beta/', 'beta'),
                       )

