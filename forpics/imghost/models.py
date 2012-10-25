from django.db import models
from thumbs import ImageWithThumbsField
from django.db.models import FileField

# Create your models here.
class Picture(models.Model):
    image =  ImageWithThumbsField(upload_to='image', sizes=((200,150),))

class Document(models.Model):
	document = FileField(upload_to='document')