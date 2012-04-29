from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'recqrd.views.home'),
	#url(r'^admin/', 'recqrd.views.admin'),
	url(r'^([ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjklmnpqrstuvwxyz123456789]{5}$)', 'recqrd.views.item' ),
	url(r'^admin/', include(admin.site.urls)),
)

