from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from courses.views import courses_list

def home(request):
	return render(request, 'index.html', {'string': 'Hello world!',
										  'second': 'dfsh dsbdfhdf'})
	#return HttpResponse('<html><head></head><body>Hello world!</body></html>') 


urlpatterns = patterns('',

    url(r'^$', home),
    url(r'^courses/', include('courses.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
