from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'recqrd.views.home', name='home'),
	url(r'^admin/', 'recqrd.views.admin', name='admin'),
	url(r'^([ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjklmnpqrstuvwxyz123456789]{5})', 'recqrd.views.item' ),
)

