from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
                       url(r'^$', 'accueil'),
                       url(r'^service/(?P<id>\d+)$', 'lire'),
                       )