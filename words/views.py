# Create your views here.
#import nltk
from words.models import Document, Sentences, Words
# mimetypes import guess_type
#from gridfs.errors import NoFile
from django.http import HttpResponse, Http404
from django.conf import settings
#from words import gridfs_storage
import datetime
# from words.models import FileUpload
from django.template import Context, loader

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    t = loader.get_template('words/index.html')
    c = Context({
        'string': 'string'
    })
    return HttpResponse(t.render(c))

def get_string(request):
  #  d = Document    
  #  define code to retrieve a document and hold in variable 
   t = loader.get_template('words/index.html')
   c = Context({
       'get_string': 'string'
   })
   return HttpResponse(t.render(c))

''' NLTK tokenize code - removed for now

f = open("/home/hamish/Documents/test.txt")
raw = f.read()
tokens = nltk.word_tokenize(raw)
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
sents = sent_tokenizer.tokenize(raw)

 d = Document(title="Manual test entry", creation_date=datetime.datetime.now(), author="Hamish",comments="NA")
 Document.objects.get()._id
for sents in sents:
    s = Sents(body=sents)
    s.save()
'''
# Grid FS File Upload in Admin code

'''if settings.DEBUG:
    # Serving GridFS files through Django is inefficient and insecure.
    # NEVER USE IN PRODUCTION!
    def serve_from_gridfs(request, path):
        try:
            gridfile = gridfs_storage.open(path)
        except NoFile:
            raise Http404
        else:
            return HttpResponse(gridfile, mimetype=guess_type(path)[0])

'''


