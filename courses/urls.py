from django.conf.urls import patterns, include, url
from courses.views import courses_list, course_item, course_view


urlpatterns = patterns('',
    url(r'^list/$', courses_list),
    url(r'^(?P<course_id>\d+)/$', course_item),
    url(r'^(?P<course_slug>[\w-]+)/$', course_view),
)
