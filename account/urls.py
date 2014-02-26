from django.conf.urls import patterns, url

#from account.views import sign_up, logout_user

urlpatterns = patterns('account.views',
    url(r'^signup/$', 'sign_up', name='signup'),
    url(r'^logout/$', 'logout_user', name='logout'),
)
