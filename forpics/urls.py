from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	
	#(r'^static/(?P<path>.*)$','django.views.static.serve',	{'document_root': 'C:/Users/Cyrille/Documents/Esiea/Info/Projet_Web/ProgWeb/v1.4/forpics/media'}),
	(r'^static/(?P<path>.*)$','django.views.static.serve',	{'document_root': '/home/ProgWeb/forpics/media'}),
	
	(r'^', include('imghost.urls')),
)
