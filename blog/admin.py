#-*- coding: utf-8 -*-
from django.contrib import admin
#from blog.models import Service, Indexeur, Feed, Freshness, Status, FeedToService, Repondeur, Page_range
from blog.models import Service, Indexeur, Feed, Status, FeedToService, Repondeur
import blog.sondes as sondes


class FeedInLine(admin.TabularInline):
    model = FeedToService
    
    
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'nom','status','type')
    list_filter = ('nom', 'status','client','type')
    search_fields = ('service_id', 'nom','mep','client')
    inlines = [
        FeedInLine,
                ]
    
    fieldsets = (
                 ('Infos',{
                          # 'classes': ['collapse','wide'],
                           'fields': ('service_id','nom','type', 'dev', 'mep','client','cdp')
                           }),
                 ('status',{
                             # 'description': 'description',
                              'fields': ('status', ('description'))
                              }),
                 
                 )
    

    def queryset(self, request):
        qs = super(ServiceAdmin, self).queryset(request)
        qs = qs.order_by('nom','service_id' ).distinct()
        return qs
   
#class StatusAdmin(admin.ModelAdmin):
#    list_display = ('nom',)
#class IndexeurAdmin(admin.ModelAdmin):
#    list_display = ('nom',)



    
admin.site.register(Service, ServiceAdmin)
admin.site.register(Indexeur)
admin.site.register(Feed)
admin.site.register(Status)
admin.site.register(Repondeur)

admin.site.register(sondes.Freshness)
admin.site.register(sondes.Page_range)
admin.site.register(sondes.Sanity)
admin.site.register(sondes.Result_count)
admin.site.register(sondes.Last_indexation)
admin.site.register(sondes.Acp)