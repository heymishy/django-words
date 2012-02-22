# This also imports the include function
from django.conf.urls.defaults import *
from words.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/$', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
#   url(r'^words/', include('words.urls')),
    url(r'^words/$', 'words.views.index'),
    url(r'^words/time$', 'words.views.current_datetime'),
    url(r'^words/db$', 'words.views.get_string'),

)

