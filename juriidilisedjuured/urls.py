from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from juriidilisedjuured import api
from juriidilisedjuured.views import home_files, NodeAutocomplete

router = DefaultRouter()
router.register(r'nodes', api.NodeViewSet, base_name='Node')

urlpatterns = [
    url(r'^node-autocomplete/$', NodeAutocomplete.as_view(), name='node-autocomplete'),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$', home_files, name='home-files'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]
