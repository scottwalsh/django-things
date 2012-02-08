from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('things.views',
    # Individual thing
    url(r'^(?P<thing_id>\d+)/$', 'detail'),
    # Things, a list of all the things on the site
    url(r'^$', 'index'),
)
