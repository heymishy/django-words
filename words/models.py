from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField
from .forms import StringListField

# Create your models here.

## Grid FS FileUpload section

'''from gridfsuploads import gridfs_storage
class FileUpload(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=gridfs_storage, upload_to='/')
'''
class SentsField(ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, StringListField, **kwargs)

class Document(models.Model):
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    author = models.CharField(max_length=100)
    sents = SentsField()
#   comments = models.CharField(max_length=200)
#   sents = ListField(EmbeddedModelField('Sents')
def __unicode__(self):
        return self.title

class Sentences(models.Model):
    body = models.TextField()

class Words(models.Model):
    word = models.CharField(max_length=80)
#   occurence = models.IntegerField)
    word_type = models.CharField(max_length=30)
def __unicode__(self):
        return self.word

