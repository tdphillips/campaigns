from django.conf import settings
from django.conf.urls import patterns, include, url


urlpatterns = patterns('campaign.views',
    url(r'^edit/$', 'create_edit_prospectus', name='create_edit_prospectus'),
)
