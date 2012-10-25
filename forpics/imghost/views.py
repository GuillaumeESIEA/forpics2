from django.shortcuts import render_to_response, get_object_or_404 
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from imghost.models import Picture
from imghost.models import Document
import time

# Create your views here.
def index(request):
	latest_picture = Picture.objects.latest('id')
	latest_document = Document.objects.latest('id')
	return render_to_response('index.html', {'latest_picture':latest_picture, 'latest_document':latest_document}, context_instance=RequestContext(request))

def picture_detail(request, picture_id):
	picture = get_object_or_404(Picture, id=picture_id)
	return render_to_response('image_detail.html', {'picture':picture})

def document_detail(request, document_id):
	document = get_object_or_404(Document, id=document_id)
	return render_to_response('document_detail.html', {'document':document})
	
def upload(request):
	if 'file' in request.FILES:
		extension = request.FILES['file'].name.split(".")[-1]
		filename = request.FILES['file'].name.split(".")[0] + "_" + str(int(time.time())) + "." + request.FILES['file'].name.split(".")[-1]
		if extension in ['bmp', 'jpg', 'jpeg', 'png']:
			picture = Picture()
			picture.image.save(filename, request.FILES['file'])
			return HttpResponseRedirect(reverse('imghost.views.picture_detail', args=[picture.id]))
		else:
			document = Document()
			document.document.save(filename,request.FILES['file'])
			return HttpResponseRedirect(reverse('imghost.views.document_detail', args=[document.id]))
	return HttpResponseRedirect(reverse('imghost.views.index', args=[]))
	
def gallery(request):
	latest_picture = Picture.objects.latest('id')
	album = Picture.objects.all()
	return render_to_response('gallery.html', {'album':album, 'latest_picture':latest_picture})
	
def gallery_doc(request):
	latest_document = Document.objects.latest('id')
	album = Document.objects.all()
	return render_to_response('gallery_doc.html',{'album':album, 'latest_document':latest_document})