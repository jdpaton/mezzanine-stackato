from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

from mezzanine.core.views import direct_to_template


admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality to
# the project's homepage.
if settings.DEBUG:
  from os.path import join, dirname, abspath                                  
  urlpatterns = patterns('',                                                 
    url(r'^media/admin/(?P<path>.*)$', 'django.views.static.serve',         
      {'document_root': abspath(join(dirname(admin.__file__), 'media')), 'show_indexes': True}),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',              
      {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),  
  )

urlpatterns += patterns("",
    ("^admin/", include(admin.site.urls)),
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    # ADD YOUR OWN URLPATTERNS *ABOVE* THE LINE BELOW.
    # ``mezzanine.urls`` INCLUDES A *CATCH ALL* PATTERN
    # FOR PAGES, SO URLPATTERNS ADDED BELOW ``mezzanine.urls``
    # WILL NEVER BE MATCHED!
    ("^", include("mezzanine.urls")),
)

# Adds ``MEDIA_URL`` to the context.
handler500 = "mezzanine.core.views.server_error"
