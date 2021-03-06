"""
Copyright (C) 2016-2020 Quasar Science Resources, S.L.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.

@package avi.urls

--------------------------------------------------------------------------------

This module provides the urls for the application.

This module provides the django urls dispachers.

@see https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.conf.urls import url, include, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from . import views
from . import views_api

# initial configuration
from avi.core.risea import risea
risea().get()

# urlpatterns configuration
## @var router
#  REST API routers
#
#  @see http://www.django-rest-framework.org/api-guide/routers/
router = routers.DefaultRouter()
router.register(r'resources', views_api.resources_list)
router.register(r'gaia_queries', views_api.gaia_queries_list)
router.register(r'hsa_queries', views_api.hsa_queries_list)
router.register(r'list_algorithms', views_api.algorithms_list)
router.register(r'plots', views_api.plot_list)
router.register(r'results', views_api.results_list)
router.register(r'alg_info', views_api.algorithms_info)
router.register(r'alg_groups', views_api.algorithms_group)

## @var api_urls
#  REST API URLs
api_urls = [
    #url(r'^', include(router.urls)),
    url(r'^resource/(?P<resource_id>[0-9]+)/$', 
        views_api.resource.as_view(),name='api-resource'),
    url(r'^samp_resource/(?P<resource_id>[0-9]+)/$', 
        views_api.resource.as_view(),name='api-samp-resource'),
    url(r'^res/(?P<resource_id>[0-9]+)/$',
        views_api.get_resource.as_view(),name='api-get_resource'),
]

api_urls = format_suffix_patterns(api_urls)

## @var urlpatterns
#  URL patterns
#
#  @see https://docs.djangoproject.com/en/2.0/topics/http/urls/
urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^', include(router.urls)),
                       url(r'^api/', include(api_urls, namespace='api')),
                       url(r'^(?P<fib>[0-9]+)$', views.create, name='create'),
                       url(r'^algorithms', views.pipeline_v2, name='pipe'),
                       url(r'^pipeline', views.pipeline, name='pipeline'),
                       url(r'^status', views.status, name='status'),
                       url(r'^ajax/send_samp_data', 
                           views.send_samp_data, name='send_samp_data'),
                       url(r'^ajax/get_results', 
                           views.get_results, name='get_results'),
                       url(r'^ajax/get_query_info', 
                           views.get_query_info, name='get_query_info'),
                       url(r'^ajax/get_query_status', 
                           views.get_query_status, name='get_query_status'),
                       url(r'^ajax/get_alg_info',
                           views.get_alg_info, name='get_alg_info'),
                       url(r'^ajax/get_plot', 
                           views.get_plot, name='get_plot'),
                       url(r'^queries/gaia', 
                           views.query_gaia, name='query_gaia'),
                       url(r'^queries/herschel', views.query_herschel, 
                           name='query_herschel'),
                       url(r'^queries/simulations', views.query_simulations, 
                           name='query_simulations'),
                       url(r'^queries/status', views.query_status, 
                           name='query_status'),
                       url(r'^queries/saved', views.query_saved, 
                           name='query_saved'),
                       url(r'^resources/filemanager', 
                           views.resources_filemanager, 
                           name='resources_filemanager'),
                       url(r'^about', views.about, name='about'),
                       url(r'^help', views.help, name='help'),
                       url(r'^contact', views.contact, name='contact'),
                       url(r'^deavi_structure', views.deavi_structure, name='deavi_structure'),
                       url(r'^tutorial', views.tutorial, name='tutorial'),
                       url(r'^debug', views.debug, name='debug'),
                       #url(r'^vr', views.vr, name='vr'),
                       url(r'^algorithm/(?P<alg_id>[-A-Za-z0-9_]+)/$', views.algorithm, name='algorithm'),
)
