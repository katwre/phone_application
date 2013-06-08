from django.conf.urls import patterns, include, url
from django.views.generic import ListView,TemplateView,FormView
from phone_app.views import *
from phone_app.forms import ProductForm

from django.conf.urls.defaults import *
from manifesto.views import ManifestView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

datetime_pattern = "\d{4}\-\d{1,2}\-\d{1,2}T\d{1,2}:\d{1,2}:\d{1,2}Z"  



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'phone_application.views.home', name='home'),
    # url(r'^phone_application/', include('phone_application.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    
    url(r'^$', FormView.as_view(template_name="home.html",form_class = ProductForm ),name="home"),      
    url(r'^integrate_database/(?P<last_date>'+datetime_pattern+')$', IntegrateDatabase.as_view(), name="integrate_database"),
    url(r'^detail_offline/$', TemplateView.as_view(template_name="detail_offline.html"),name="detail_offline"), 
    
    url(r'^manifest\.appcache$', ManifestView.as_view(), name="cache_manifest"),

    )

    
      
    
    
    
    
    
    