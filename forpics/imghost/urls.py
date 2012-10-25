from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'imghost.views.index'),
	(r'^image/(?P<picture_id>\d+)/$', 'imghost.views.picture_detail'),
	(r'^upload/$', 'imghost.views.upload'),
	(r'^gallery/$', 'imghost.views.gallery'),
	(r'^gallery_doc/$', 'imghost.views.gallery_doc'),
	(r'^document/(?P<document_id>\d+)/$', 'imghost.views.document_detail'),
)