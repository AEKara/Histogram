"""Histogram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from Frequency_Of_Words.views import histogram
from Frequency_Of_Words.views import histogram
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^histogram/(?P<offset>.*)/$', histogram), #get the url to insert as a parameter in the view.
    #(r'^histogram/(\d{1,20})/$',histogram),
]
