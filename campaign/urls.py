from django.conf import settings
from django.conf.urls import patterns, include, url


urlpatterns = patterns('campaign.views',
    url(r'^new/$', 'create_prospectus', name='create_prospectus'),
    url(r'^(?P<prospectus_id>\d+)$', 'view_prospectus', name='view_prospectus'),
    url(r'^(?P<prospectus_id>\d+)/edit/$', 'edit_prospectus', name='edit_prospectus'),
)
