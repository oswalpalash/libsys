from django.conf.urls.defaults import *
from mysite import views
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from blog.views import archive
urlpatterns = patterns('views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
	url(r'^hello/$',views.hello),
	url(r'^time/$',views.current_datetime),
	url(r'^another-time-page/$',views.current_datetime),
	url(r'^time/plus/(\d{1,2})/$',views.hours_ahead),
	url(r'^search-form/$', views.search_form),
	(r'^search/$', views.search),
	url(r'^contact/$',views.contact),
	(r'^(foo)/$', views.foobar_view),
    (r'^(bar)/$', views.foobar_view),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^archive/$', views.archive),
    
)
