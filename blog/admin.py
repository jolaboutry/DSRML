#-*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Service, Indexeur, Feed, Freshness, Status, FeedToService, Repondeur


class FeedInLine(admin.TabularInline):
    model = FeedToService
    
    
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'nom','status')
    list_filter = ('nom', 'status','client')
    search_fields = ('service_id', 'nom','mep','client')
    inlines = [
        FeedInLine,
                ]
    
    fieldsets = (
                 ('Infos',{
                          # 'classes': ['collapse','wide'],
                           'fields': ('service_id','nom','dev', 'mep','client','cdp')
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
admin.site.register(Freshness)
admin.site.register(Status)
admin.site.register(Repondeur)