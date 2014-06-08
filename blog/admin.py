#-*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Service, Status, Indexeur
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'nom','status')
    list_filter = ('nom', 'status', 'indexeur')
    search_field = ('service_id', 'nom')
    
    fieldsets = (
                 ('Infos',{
                          # 'classes': ['collapse','wide'],
                           'fields': ('service_id','nom')
                           }),
                 ('instance',{
                             # 'description': 'description',
                              'fields': ('status', ('description'),('indexeur'))
                              }),
                 )
    def queryset(self, request):
        qs = super(ServiceAdmin, self).queryset(request)
        qs = qs.order_by('nom','service_id' ).distinct()
        return qs
   


    
admin.site.register(Service, ServiceAdmin)
admin.site.register(Status)
admin.site.register(Indexeur)