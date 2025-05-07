# headliner_project/urls.py
from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static # For serving media in dev

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap # Wagtail sitemap

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('sitemap.xml', sitemap), # Wagtail sitemap
    # path('search/', include('haystack.urls')), # If using Haystack/Elasticsearch
    # Add other app URLs here
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns() # Serve static files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Serve media files

urlpatterns += [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern.
    path("", include(wagtail_urls)),
]
